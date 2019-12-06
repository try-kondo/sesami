# Door Sensor
# Option Change

from io import open
import sys
import dir_path

if __name__ == '__main__':
    args = sys.argv
    path = dir_path.etc_path()

    if 3 == len(args):

        with open(path) as f:
            list = f.readlines()

        length = len(list)

        tar = '[' + args[1] + ']='

        for i in range(length):
            index = list[i].find(tar)
            if index != -1:
                tar_opt = list[i]
                tar_opt_len = len(tar_opt)
                tar_tmp = tar_opt[:len(tar) - tar_opt_len]
                list[i] = tar_tmp + args[2]

                with open(path, 'w', encoding='utf-8') as f_w:
                    for r in list:
                        if len(r) != 1:
                            # r = r + '\n'
                            r = r.rstrip()
                            r = r + '\n'
                            f_w.write(r)
                break
    else:
        print 'args not found'
