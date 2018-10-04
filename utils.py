import zipfile

def unzip(path_from, path_to):
	z_file = zipfile.ZipFile(path_from,'r')
	z_file.extractall(path_to)
	z_file.close()