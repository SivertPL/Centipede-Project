import zipfile
import shutil

#error, info, warning



def error(a):
	print("[Error] " + a)

def info(a):
	print("[Info] " + a)
	
def warning(a):
	print("[Warning] " + a)

#-----------------------------------------

def unzip(path_from, path_to):
	z_file = zipfile.ZipFile(path_from,'r')
	z_file.extractall(path_to)
	z_file.close()
