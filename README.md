# liangongbao

## 安装

1. 首先需要python3环境,官网下载<https://www.python.org/downloads/>

2. 安装mitmproxy

   `pip3 install mitmproxy`



或者直接在mitmproxy官网https://mitmproxy.org/下载安装程序安装.

这里要感谢[@8188](https://github.com/8188)同学的提醒

## 使用

1. 启动脚本

   `mitmdump -s aqy.py -p 8888 "~d h5we.lgb360.com"`

2. 打开手机进入无线网设置代理,IP设为运行脚本机器的IP地址,端口设为8888,也可以根据需要进行修改.

3. 浏览器打开<mitm.it>下载证书安装.

## 说明

截止到6月7日已经记录了188题目, 欢迎大家继续收集.

可以提PR我来合并.