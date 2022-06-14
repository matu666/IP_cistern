import sqlite3
from copy_ip.conn import read_yaml


# 创建数据库方法
def create_db():
    """
    创建数据库
    :return:
    """
    # 创建数据库
    db = sqlite3.connect(read_yaml()["db"])
    # 创建游标
    cursor = db.cursor()
    return cursor, db


# 创建表方法
def create_table():
    """
    创建表
    :return:
    """
    # 创建数据库
    cursor, db = create_db()
    # 创建表 ip= 服务器ip port=端口 protocol=协议 country=国家，ip不能为空和唯一
    cursor.execute("create table acting(ip_port varchar(20) primary key,ip varchar(15) not null,port int(6) not null,  protocol varchar(6), country varchar(10))")
    # 关闭数据库
    db.close()


# 插入数据方法
def insert_data(ip_port,ip, port, protocol, country):
    """
    插入数据
    :param ip_port: ip:port
    :param ip: ip地址
    :param port: 端口
    :param protocol: 协议
    :param country: 地区
    :return:
    """
    db = None
    try:
        # 创建数据库
        cursor, db = create_db()
        # 插入数据 ip, port,  protocol, country
        cursor.execute("insert into acting values('%s','%s',%d,'%s','%s')" % (ip_port,ip, port, protocol, country))

        # cursor.execute("insert into ip values('%s',)" %)
        db.commit()
    except Exception as e:
        # print(str(ip_port) + "已存在")
        pass
    finally:
        # 关闭数据库
        db.close()


# 查询数据方法
def select_data(country=read_yaml()["area"]):
    """
    查询数据
    :return:
    """
    # 创建数据库
    cursor, db = create_db()
    # 查询数据
    if country == "ALL":
        cursor.execute("select * from acting")
    elif country == "CN":
        cursor.execute("select * from acting where country='%s'" % country)
    elif country == "NCN":
        cursor.execute("select * from acting where country!='CN'")
    else:
        data = ['只能查询中国或者全部']
    # 获取数据
    data = cursor.fetchall()
    # 关闭数据库
    db.close()
    return data


# 删除所有数据方法
def delete_data():
    """
    删除数据
    :return:
    """
    # 创建数据库
    cursor, db = create_db()
    # 删除数据
    cursor.execute("delete from acting")
    db.commit()
    # 关闭数据库
    db.close()


# 删除某一条数据方法
def delete_one_data(ip_port):
    """
    删除数据
    :return:
    """
    # 创建数据库
    cursor, db = create_db()
    # 删除数据
    cursor.execute("delete from acting where ip_port='%s'" % (ip_port))
    db.commit()
    # 关闭数据库
    db.close()