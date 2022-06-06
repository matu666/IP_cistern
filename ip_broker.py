from copy_ip.ip_pool import while_loop
from copy_ip.kill import process_kill

# ql配置文件路径默认是 /root/ql/config/config.sh
path = '/root/ql/config/config.sh'
# ql要修改行的行数
line = int(1)


if __name__ == '__main__':
    process_kill("ip_broker.py")
    while_loop(path, line)

