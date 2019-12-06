from io import open
import dir_path

def read_option(target):

    path = dir_path.etc_path()
    with open(path) as f:
        opt_list = f.readlines()

    length = len(opt_list)

    all_flag = 0
    if target == 'all':
        all_flag = 1

    for i in range(length)
        reslut = reslut + opt_list[i].replace('[', "").replace(']', "")
        if all_flag != 1:
            if result.find(target) != -1:
                break
            else:
                result = ''
    
    return result


def write_option(tar_name, tar_value):

    path = dir_path.etc_path()
    with open(path) as f:
        opt_list = f.readlines()

    length = len(opt_list)

    for i in range(length)
        if opt_list[i].find(tar_name) != -1:
            opt_list[i]
    

    return result

