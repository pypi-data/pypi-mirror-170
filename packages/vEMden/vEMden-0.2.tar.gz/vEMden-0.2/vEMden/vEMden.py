import argparse
import distutils
import FiReTiTiPyLib.FiReTiTiPyTorchLib as Fptl
import FiReTiTiPyLib.FiReTiTiPyTorchLib.FiReTiTiPyTorchLib_Datasets as Datasets
import FiReTiTiPyLib.FiReTiTiPyTorchLib.FiReTiTiPyTorchLib_Denoiser as Denoiser
import FiReTiTiPyLib.FiReTiTiPyTorchLib.FiReTiTiPyTorchLib_Losses as Losses
import FiReTiTiPyLib.IO.IOColors as Colors
import FiReTiTiPyLib.Normalizers as Normalizer
import FiReTiTiPyLib.PyTorch_Models as Models
import FiReTiTiPyLib.PyTorch_Models.Denoising as Denoisers
import gc
import os
import random
import sys
import time
import torch
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.nn as nn
import torchvision.transforms as Transformer

from torch.utils.data import DataLoader
from torchvision.transforms import Compose



def str2bool(v):
	return bool(distutils.util.strtobool(v))


parser = argparse.ArgumentParser(description='Volume Electron Microscopy Denoiser (vEMden) Example')
parser.add_argument("--dataDir", type=str, default="./Data/", help="Path to the data to denoise.")
parser.add_argument('--batchSize', type=int, default=12, help='Training/Inference batch size. Default=12')
parser.add_argument('--nIterations', type=int, default=1001, help='Minimum number of iteration (weights update) to '
												+ 'perform. Minimum recommended: 500 for NRRN and 1000 for DenoiseNet.')
parser.add_argument('--lr', type=float, default=0.0001, help='Learning Rate. Default=0.0001.')
parser.add_argument('--nThreads', type=int, default=4, help='Number of threads to use by the data loaders.')
parser.add_argument('--seed', type=int, help='Random seed.')
#parser.add_argument('--cuda', action=argparse.BooleanOptionalAction, help='Use cuda?')
#parser.add_argument('--cuda', type=bool, default=True, help='Use cuda? Default=True')
#parser.add_argument('--cuda', action='store_true', help='Use cuda? Default=True')
parser.add_argument('--cuda', type=str2bool, nargs='?', const=True, default=False, help='Use cuda? Default=False')
#parser.add_argument("--resume", default="", type=str, help="Path to checkpoint (default: none)")
#parser.add_argument("--start_epoch", default=1, type=int, help="Manual epoch number (useful on restart)")
parser.add_argument("--net", default="NRRN", type=str, help="net could be: NRRN(default) | DenoiseNet | "
															+ "PathToSavedModel")
parser.add_argument("--nBlocks", default=4, type=int, help="Number of denoising blocsk/layers (model depth)."
															+ " Defaults=4.")
parser.add_argument("--nFeaturesMaps", default=32, type=int, help="Number of features maps (model width). Defaults=32.")
parser.add_argument("--trainingSize", default=-1, type=int, help="Number of pairs/triplets in the dataset used for "
														+ "training. Defaults=-1, which means all images will be used.")
parser.add_argument("--cropSize", default=256, type=int, help="The size of the crops/patches used during training and "
															+ "inference. Defaults=256.")
parser.add_argument('--debug', type=str2bool, nargs='?', const=True, default=False, help='Use debug mode?')



def _InputTransform_(cropSize):
	"""
		Performs transformation on the input image
	"""
	return Compose([Transformer.RandomCrop(cropSize),
					Transformer.RandomHorizontalFlip(),
					Transformer.RandomVerticalFlip()])



def _TrainSingleEpoch2_(model, optimizer, criterion, device, epoch, DL, verbose: bool = True):
	epoch_loss = 0.0
	tstart = time.time()
	for iteration, batch in enumerate(DL, 1):
		optimizer.zero_grad()
		
		image, imnext = batch[0].to(device), batch[1].to(device)
		
		out = model(image)
		
		loss = criterion(out, imnext)
		
		epoch_loss += loss.item()
		loss.backward()
		optimizer.step()
	
	aveloss = epoch_loss / len(DL)
	if verbose:
		print("---> Epoch {} Complete: Avg. Loss = {:.5f} in {:.5f}s.".format(epoch, aveloss, time.time() - tstart))
	return aveloss



def _TrainSingleEpoch3_(model, optimizer, criterion, device, epoch, DL, verbose: bool=True):
	epoch_loss = 0.0
	tstart = time.time()
	for iteration, batch in enumerate(DL, 1):
		optimizer.zero_grad()
		
		imprev, image, imnext = batch[0].to(device), batch[1].to(device), batch[2].to(device)
		
		x = torch.cat((imprev, image), dim=1) # concat the 2 images on the channel dim => (batch,2,256,256)
		y = torch.cat((imnext, image), dim=1)
		
		out_x = model(x)
		out_y = model(y)

		loss = criterion(imprev, imnext, out_x, out_y)

		epoch_loss += loss.item()
		loss.backward()
		optimizer.step()
		
	aveloss = epoch_loss / len(DL)
	if verbose:
		print("---> Epoch {} Complete: Avg. Loss = {:.5f} in {:.5f}s.".format(epoch, aveloss, time.time()-tstart))
	return aveloss



def _Run_(dataDir: str, seed: int, net: str, nBlocks: int, nFeaturesMaps: int, cuda: bool, lr: float, batchSize: int,
			nIterations: int, trainingSize: int, cropSize: int, nThreads: int, debug: bool):
	
	print(Colors.Colors.GREEN + '\n=====> Checking parameters' + Colors.Colors.RESET)
	if seed is not None:
		random.seed(seed)
		torch.manual_seed(seed)
		cudnn.deterministic = True
		print(Colors.Colors.RED + '\nWARNING - ' + Colors.Colors.RESET + 'You have chosen to seed training. '
				'This will turn on the CUDNN deterministic setting, which can slow down your training considerably!\n')
	
	if cuda and not torch.cuda.is_available():
		raise Exception("No GPU found but option '--cuda' enabled, please disable cuda option '--cuda=False' "
						"or run with a GPU.")
	print("Parameters preliminary ckecking done.")
	
	
	print(Colors.Colors.GREEN + '\n=====> Building model' + Colors.Colors.RESET)
	model, nInputs, ModelType = Denoisers.getDenoisinNetwork(NET_TYPE=net, nbBlocks=nBlocks,
															FeatureMaps=nFeaturesMaps)
	if model is None:
		Training = False
		print("Loading previously trained model... ", end='')
		try:
			#model = torch.load(opt.net, map_location=torch.device("cpu")) # Does not work with DataParallel.
			modelname = os.path.basename(net)
			elements = modelname.split('_')
			nBlocks = int(elements[2][8:len(elements[2])])
			nMaps = int(elements[3][6:len(elements[3])])
			if "nrrn" in net.lower():
				Type = "NRRN"
			elif "denoisenet" in net.lower():
				Type = "DenoiseNet"
			else:
				print(Colors.Colors.RED + '\nERROR - Unknown denoising model type.\n' + Colors.Colors.RESET)
				raise Exception('Unknown denoising model type.')
			model, nInputs, ModelType = Denoisers.getDenoisinNetwork(NET_TYPE=Type, nbBlocks=nBlocks, FeatureMaps=nMaps)
			model.load_state_dict(torch.load(net, map_location='cpu'))
			print("succesfully.")
			print("Denoising model type = " + ModelType)
		except:
			print(Colors.Colors.RED+"\nERROR - '" + net + "' does not contain a valid model."+Colors.Colors.RESET)
			sys.stdout.flush()
			raise Exception("'" + net + "' does not contain a valid model.")
	else:
		Training = True
		print("succesfully.")
	
	if Training:
		print("The model will be trained before denoising the dataset.")
	else:
		print("Model already trained, so skipping training.")
	
	
	print(Colors.Colors.GREEN + '\n=====> Checking environment' + Colors.Colors.RESET)
	device = Fptl.getDevice(cuda)
	model = Models.DataParallel(model)
	model.to(device)
	
	
	print("Model successfully linked to environment.")
	print("Environment checked.")
	
	
	normalizer = Normalizer.CenterReduce(MaxValue=255.0)
	
	
	if Training:
		print(Colors.Colors.GREEN + '\n=====> Creating DataSet and DataLoader' + Colors.Colors.RESET)
		
		criterion = nn.MSELoss().to(device) if nInputs == 1 else Losses.N2NLoss().to(device)
		TrainSingleEpoch = _TrainSingleEpoch2_ if nInputs == 1 else _TrainSingleEpoch3_
		decay = 0.0001 if nInputs == 1 else 0.0
		optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=decay)
		scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.5) if nInputs == 3 else None
		print("Optimizer, loss and scheduller created.")
		
		path = dataDir
		dataset = Datasets.NRRN(path, normalizer=normalizer, nInputs=nInputs, train=True, datasetSize=trainingSize,
								transformations=_InputTransform_(cropSize), Debug=debug)
		if debug:
			for i in range(dataset.__len__()): # Quick dataset check.
				if nInputs == 1:
					im, nextim = dataset.__getitem__(i)
				else:
					previm, im, nextim = dataset.__getitem__(i)
		print("Dataset created. Size = " + str(dataset.__len__()))
		
		TrainingDataLoader = DataLoader(dataset=dataset, num_workers=nThreads, batch_size=batchSize,
										drop_last=True, shuffle=True)
		print("DataLoader created.")
		
		
		print(Colors.Colors.GREEN + '\n=====> Training' + Colors.Colors.RESET)
		nEpochs = int(nIterations / int(dataset.__len__() / batchSize)) + 1
		print("Training configuration:")
		print(" - Minimum " + str(nIterations) + " iterations (weight updates) requested")
		print(" - Batch size = " + str(batchSize))
		print(" ---> Number of epochs = " + str(nEpochs))
		print(" ---> %d iterations per epoch" % (int(dataset.__len__() / batchSize)))
		print(" - Crop size = " + str(cropSize))
		print(" - Learning rate = " + str(lr))
		print(" - Cuda = " + str(True if cuda else False))
		print(" - Number of input image(s) = " + str(nInputs))
		
		for epoch in range(0, nEpochs):
			TrainSingleEpoch(model, optimizer, criterion, device, epoch, TrainingDataLoader)
			if scheduler is not None:
				scheduler.step()
		print("Training done.")
		
		year, month, day, hour, minutes = map(int, time.strftime("%Y %m %d %H %M").split())
		name = "Denoising_" + ModelType + "_nBlocks=" + str(nBlocks) + "_nMaps=" + str(nFeaturesMaps) + \
			"_Date=" + str(year) + "." + str(month) + "." + str(day) + "." + str(hour) + "h" + str(minutes) + ".pt"
		Models.SaveStateDict(model, name)
		sys.stdout.flush()
		
		del criterion
		del scheduler
		del optimizer
		del TrainingDataLoader
		del dataset
		if device == "cuda":
			torch.cuda.empty_cache()
		gc.collect()
	
	
	print(Colors.Colors.GREEN + '\n=====> Denoising / Inference' + Colors.Colors.RESET)
	
	model.eval()
	
	print("Denoising / Inference configuration:")
	print(" - Batch size = " + str(batchSize))
	print(" - Crop size = " + str(cropSize))
	print(" - Cuda = " + str(True if cuda else False))
	print(" - Number of input image(s) = " + str(nInputs))
	sys.stdout.flush()
	
	path = dataDir
	if path[len(path)-1] == '/':
		path = path[0:len(path)-1]
	
	dataset = Datasets.NRRN(path, nInputs=nInputs, train=False,	Debug=debug)
	
	denoiser = Denoiser.Denoiser(verbose=False)
	denoiser.Denoise(dataset, model, nInputs=nInputs, CropSize=cropSize, BorderEffectSize=nBlocks+5,
					BatchSize=batchSize, Device=device, Normalizer=normalizer,
					ResultsDirPath=path + " - Denoised " + ModelType)
	
	print(Colors.Colors.GREEN + "\nAll Done." + Colors.Colors.RESET)



def Denoise(parameters: dict=None):
	if parameters is not None: # Running from script with parameters in a dict.
		args = []
		for key in parameters.keys():
			args.append("--"+str(key)+"="+str(parameters[key]))
		opt = parser.parse_args(args)
		if opt.nThreads != 0:
			print(Colors.Colors.RED + "WARNING - " + Colors.Colors.RESET + " nThreads != 0 when called from script." +
									" This might generate an error. It'll be fixed in futur release. Use command " +
									"line or set nThreads to 0.\n")
	else: # Running from command line
		opt = parser.parse_args()
	
	if opt.debug:
		print("Debugging mode activated.")
		print("Command line arguments:")
		print(opt)
	
	_Run_(opt.dataDir, opt.seed, opt.net, opt.nBlocks, opt.nFeaturesMaps, opt.cuda, opt.lr, opt.batchSize,
			opt.nIterations, opt.trainingSize, opt.cropSize, opt.nThreads, opt.debug)





if __name__ == '__main__':
	print("Let's go manual!")
	parameters = {'dataDir': "/Users/firetiti/Downloads/EM/Denoising/Example/Registered Crop 1024x1024/",
				'batchSize': 16,
				'nIterations': 23,
				'lr': 0.0001,
				'nThreads': 2,
				#'seed': 13,
				'cuda': False,
				'net': '/Users/firetiti/Downloads/EM/Denoising/Example/Denoising_DenoiseNet_nBlocks=13_nMaps=13_Date=2022.8.31.12h57.pt',#'denoiseNet',
				'nBlocks': 7,
				'nFeaturesMaps': 16,
				'trainingSize': -1,
				#'cropSize': 256,
				'debug': True}
	#Denoise(parameters=parameters)
	Denoise()
