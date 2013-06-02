import os
import errno

d = 'dirname'
f = 'filename'

def ensure_dir(f):


def make_sure_path_exists(path):
	try:
	os.makedirs(path)
	except OSError as e:
		if e.errno == errno.EEXIST: #path already exists
			##do sth
