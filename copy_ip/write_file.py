# 写入文件
import random

from copy_ip.conn import read_yaml
from copy_ip.other.log import log_ip
from copy_ip.pysqlit.py3 import select_data

data = read_yaml()
sql = select_data()


def get_random_ip():
    """
    如果节点都不可以用，就把写入文件空，让ql使用主机IP，
    添加路径异常判断，如果路径不存在，打印路径不存在
    :return:
    """
    random_ip = None
    try:
        # 获取随机IP，如果没有IP，就把写入文件空，让ql使用主机IP
        random_ip = random.randint(len(sql))
        random_ip = 'export ALL_PROXY=' + sql[random_ip][3] + "://" + sql[random_ip][0]
    except Exception as e:
        # 代理添加为空，表示代理池IP都不可用
        print("代理池IP都不可用",str(e))
        random_ip = "export ALL_PROXY= ''"
    print("本次IP是", random_ip)
    log_ip("本次IP是" + str(random_ip))
    # 写入文件
    try:
        f = open(data['path'], 'r+', encoding='utf-8')
        flist = f.readlines()
        # ql行数从一开始，python读取从零开始
        try:
            flist[data['line'] - 1] = '{}\n'.format(random_ip)
            log_ip("写入文件成功,添加代理是: " + str(random_ip))
            f = open(data['path'], 'w+', encoding='utf-8')
            f.writelines(flist)
        except Exception as e:
            log_ip("异常问题，get_random_ip" + str(e))
        f.close()
    except Exception as e:
        # 打印明显异常信息
        log_ip("异常问题，get_random_ip" + str(e))
