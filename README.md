# 青龙使用代理池来避免黑IP问题
## 此文档默认为最新文档，同步脚本更新此文档
## 需要下载 ip_broker.py 和 copy_ip目录的文件，否则报错
## [青龙代理视频演示](https://youtu.be/zGoirXzPMQk)
## 下面是在青龙里面运行py文件检测到的IP
<img src="./img/demo.jpg" alt="">
<br>
使用的库
根据需代码提示缺少依赖添加

```
pip3 install requests
pip3 install datetime
pip3 install time
pip3 install random
pip3 install json
```

### 在脚本的第10行改成自己的配置文件地址，一般青龙目录都是这个
path = '/root/ql/config/config.sh'
### 在脚本的第12改成代理添加的行数，
line = int(134)
请查看config.sh配置文件查看自己需要添加哪一行，选择空白行添加

### 查看是否添加成功
在青龙脚本管理-->新建脚本-->ip.py
把下内容进去，然后调试，脚本选择python,然后运行，如果显示代理IP表示添加成功

```python
import requests
aas = requests.get("https://ip.tool.lu/")
print("检测到的IP", aas.text)
```

代理脚本会根据抓取的代理池更新而延迟一秒钟更新，代理池大部分代理可用请放心使用
<br>
线程守护运行脚本
```
nohup python3 ip_broker.py &
```



