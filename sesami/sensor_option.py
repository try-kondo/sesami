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
            print '--- For i ---'
            print 'i=',i
            print 'length=',length
            print 'list[i]=',list[i]
            print 'index=',index
            print 'tar=',tar
            if index != -1:
                tar_opt = list[i]
                tar_opt_len = len(tar_opt)
                tar_tmp = tar_opt[:len(tar) - tar_opt_len]
                list[i] = tar_tmp + args[2]

                with open(path, 'w', encoding='utf-8') as f_w:
                    for r in list:
                        print '--- For r ---'
                        if len(r) != 1:
                            # r = r + '\n'
                            r = r.rstrip()
                            r = r + '\n'
                            print 'Write=',r
                            f_w.write(r)
                print 'Write:',args[1],'=',args[2]
                break
            else:
                print 'index error'
    else:
        print 'args not found'
