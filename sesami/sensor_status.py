# Door Sensor
# Option Status

from io import open
import sys
import dir_path


def get_status(target, path):
	with open(path) as f:
	        s = f.read()

	str_ser = '[' + target + ']='
	index = s.find(str_ser)
	if index != -1:
		tmp = s
		s_start = tmp.find(str_ser) + len(str_ser)
		s_end = tmp.find('\n', s_start)
		
		result = s[s_start:s_end]
	else:
		result = 'Not Found'

	return result


if __name__ == '__main__':
	
	args = sys.argv
	path = dir_path.etc_path()

	if 1 == len(args):
		with open(path) as f:
			list = f.readlines()

		length = len(list)

		for i in range(length):
			tmp = list[i]
			if tmp.find('[') != -1:
				s_start = tmp.find('[') + 1
				s_end = tmp.find(']')
				tar = tmp[s_start:s_end]
				ans = get_status(tar, path)
				print tar , ans
	else:
		length = len(args)
		for i in range(length):
			if i != 0:
				tar = args[i]
				ans = get_status(tar, path)
				print tar , ans
