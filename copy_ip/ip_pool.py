import json
import requests
from copy_ip.other.heade import get_user_agent
from copy_ip.other.log import log_ip
from copy_ip.pysqlit.py3 import insert_data, delete_data, select_data


def get_ip():
    """
    爬取的IP池地址
    :return:
    """
    # 删除数据库内容
    delete_data()
    log_ip("删库跑路完毕")
    print("删库跑路完毕")
    delete_data()
    select_data()
    print("代理池现在清空" + str(select_data()))
    # 获取网站数据
    url = 'https://uu-proxy.com/api/free'
    try:

        strhtml = requests.get(url, headers=get_user_agent(), verify=False)
        data = json.loads(strhtml.text)
        for i in range(len(data['free']['proxies'])):
            # 下面是 地址、端口号、协议、支持HTTPS
            ip = data['free']['proxies'][i]['ip']
            port = data['free']['proxies'][i]['port']
            protocol = data['free']['proxies'][i]['scheme']
            country = "CN"
            # 添加的数据库
            insert_data(ip + ':' + str(port), ip, port, protocol, country)
        # 关闭爬取网站
        strhtml.close()

    except Exception as e:
        print("异常提示,ip_pool>get_ip: " + str(e))
        log_ip("异常提示,ip_pool>get_ip: " + str(e))
