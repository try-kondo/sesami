from io import open
import sys
import time
import datetime

import dir_path
import check_gpio_bcm
import sesami_control


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
            print 'len(ser_enable) =', len(ser_enable)
            print 'len(opt_list[i]) =', len(opt_list[i])
            opt_enable = tmp[len(ser_enable)-len(tmp):]
        elif opt_list[i].find(ser_timer) != -1:
            tmp = opt_list[i]
            tmp = tmp.rstrip()
            print 'len(ser_timer) =', len(ser_timer)
            print 'len(opt_list[i]) =', len(opt_list[i])
            opt_timer = tmp[len(ser_timer)-len(tmp):]


    print opt_enable
    print opt_timer

    if opt_enable == 'True':
        print datetime.datetime.now()
        time.sleep(int(opt_timer))
        print datetime.datetime.now()
        sesami_control.sesami_lock()

    else:
        print 'Sensor False'
        sys.exit

