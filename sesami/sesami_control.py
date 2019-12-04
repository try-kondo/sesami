from io import open
import sys
import time
import subprocess

import dir_path
import check_gpio_bcm


if __name__ == '__main__':

    i_bcm = check_gpio_bcm.gpio_input_bcm(18)
    if i_bcm != 1:
        sys.exit()

    path = dir_path.etc_path()

    with open(path) as f:
        opt_list = f.readlines()

    length = len(opt_list)

    ser_enable = '[Enable]='
    ser_timer = '[Timer]='
    for i in range(length):
        if opt_list[i].find(ser_enable) != -1:
            tmp = opt_list[i]
            tmp = tmp.rstrip()
            opt_enable = tmp[len(ser_enable)-len(opt_list[i]):]
        elif opt_list[i].find(ser_timer) != -1:
            tmp = opt_list[i]
            tmp = tmp.rstrip()
            opt_timer = tmp[len(ser_timer)-len(opt_list[i]):]


    print opt_enable
    print opt_timer

    if opt_enable == 'True':
        time.sleep(opt_timer)
        res = subprocess.call('python status.py')

    else:
        print 'Sensor False'
        sys.exit

