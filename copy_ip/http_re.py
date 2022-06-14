import threading

import requests

from copy_ip.other.heade import get_user_agent
from copy_ip.pysqlit.py3 import select_data, delete_one_data


def http_request(http_ip_port, ip_port):
    """
    检测节点是否可用
    :param http_ip_port: 测试的节点
    :param ip_port: 如果不可用删除的索引
    :return:
    """
    proxies = {
        'http': http_ip_port,
        'https': http_ip_port
    }
    try:
        # 检测节点是否可用.多次检测，如果可用，就把节点添加到字典中，检测多个防止代理无效，主要用于京东使用代理验证京东网址是否支持代理
        # 请求超过3秒，就认为节点不可用
        output1 = requests.get("https://plogin.m.jd.com/", proxies=proxies, headers=get_user_agent(), timeout=2)
        output2 = requests.get("https://www.zhihu.com/", proxies=proxies, headers=get_user_agent(), timeout=2)
        output3 = requests.get("https://www.jd.com/", proxies=proxies, headers=get_user_agent(), timeout=2)
        # 关闭连接
        output3.close()
        output2.close()
        output1.close()
        # 修改一行代码
        # https_ip_port = 'export ALL_PROXY=' + http_ip_port
        # insert_data(https_ip_port)
        # print("可用的代理IP：" + http_ip_port)
    except Exception as e:
        # 不做任何输出,删除不可用的节点
        delete_one_data(ip_port)
        pass


# 使用多线程检测代理IP的可用性
def check_ip():
    sq = select_data()
    threads = []
    for i in sq:

        t = threading.Thread(target=http_request, args=(i[3] + "://" + i[0], i[0],))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("所有线程都结束了")
    print(select_data())

