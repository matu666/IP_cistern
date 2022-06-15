import re

import requests

from copy_ip.other.heade import get_user_agent
from copy_ip.other.log import log_ip
from copy_ip.pysqlit.py3 import insert_data


def get_git_ip():
    try:
        reps = requests.get("https://gh.fakev.cn/fate0/proxylist/blob/master/proxy.list", headers=get_user_agent())
        # 设置编码
        reps.encoding = "utf-8"
        re1 = reps.text

        # 正则表达式
        # 分别是IP，端口，类型，国家
        re_ip = re.compile(r'host&quot;: &quot;(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        re_port = re.compile(r'&quot;port&quot;: (\d{2,6})')
        re_country = re.compile(r'&quot;country&quot;: &quot;(\w+)')
        re_type = re.compile(r'&quot;type&quot;: &quot;(\w+)')

        http_ip = re_ip.findall(re1)
        http_port = re_port.findall(re1)
        http_country = re_country.findall(re1)
        http_type = re_type.findall(re1)
        # print(len(http_ip))
        # print(len(http_port))
        # print(len(http_country))
        # print(len(http_type))
        for i in range(len(http_ip)):
            # 创建字典，里面存放所有网络协议,原因https 不能使用,但是转换成http协议可以使用
            http_ip_type = {"http": "http", "https": "http", "socks": "socks", "socks4": "socks4", "socks5": "socks5"}
            insert_data(http_ip[i] + ':' + http_port[i], http_ip[i], int(http_port[i]), http_ip_type[http_type[i]],
                        http_country[i])
    except Exception as e:
        print("异常问题，git_poxy: " + str(e))
        log_ip("异常问题，git_poxy: " + str(e))
