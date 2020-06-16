from analysis.utils.option import Options
import os
import time

opt = Options()


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def upload_files():
    base_path = opt.txt_dir_path
    today = time.gmtime(time.time()).tm_mday
    cur_time = round(time.time() * 1000000)

    save_dir = base_path + '%d/%d/' % (today, cur_time)

    mkdir(save_dir)

    return save_dir


def read_text(path, encoding='utf-8'):
    with open(path, encoding=encoding) as f:
        result = f.read()

    return result
