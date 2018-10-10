## UNZIP DOCX & METADATA READ 
import zipfile
import os 

def mktmp():
	current_path = os.path.dirname(os.path.realpath(__file__))
	directory = os.path.join(current_path, "tmp")
	if not os.path.exists(directory):
		os.makedirs(directory)
	return directory


def unzip(f):
	dir = mktmp()
	zip_ref = zipfile.ZipFile(f, 'r')
	zip_ref.extractall(dir)
	zip_ref.close()

def parse(f):
	tmp = mktmp()
	# IMPORT XML MINIDOM API & PARSE METADATA




