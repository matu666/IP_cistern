from threading import Timer

from copy_ip.git_poxy import get_git_ip
from copy_ip.http_re import check_ip
from copy_ip.ip_pool import get_ip
from copy_ip.write_file import get_random_ip


def while_loop():
    """
    循环任务
    :return:
    """
    # 获取代理
    get_ip()
    get_git_ip()
    # 测试代理
    check_ip()
    # 写入文件
    get_random_ip()
    # 定时任务，300 更新一次，可自己改
    timer(300)

def timer(delay):
    """
    定时任务
    :param delay: 多少秒后执行
    :return:
    """
    hit = " "
    t = Timer(delay, while_loop, ())  # 三个参数分别是：延迟时间 调用函数 (传入调用函数的参数（必须是tuple）)
    t.start()
if __name__ == '__main__':
    while_loop()