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
        list = f.readlines()

    length = len(list)

    ser_enable = '[Enable]='
    ser_timer = '[Timer]='
    for i in range(length):
        if len(i).find(ser_enable):
            opt_enable = list(i)[:len(list(i)-len(ser_enable))]
        elif len(i).find(ser_timer):
            opt_timer = list(i)[:len(list(i)-len(ser_timer))]

    if opt_enable == 'Enable':
        time.sleep(opt_timer)
        res = subprocess.call('python lock.py')

    else:
        print 'Sensor False'
        sys.exit

