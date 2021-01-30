import os
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--path', type=str, default='/home/')
	config = parser.parse_args()
	path = config.path
	print(path)
	list_dir = os.listdir(path)
	type_dict = {'jpg':0, 'png':0, 'gif':0, 'pdf':0} 
	for fn in list_dir:
		suffix = fn.split('.')[-1]
		if suffix not in type_dict.keys():
			continue
		type_dict[suffix] += 1

	for key,values in  type_dict.items():
		if values==0:
			continue
		print(values, key, 'files')


if __name__ == '__main__':
    main()






