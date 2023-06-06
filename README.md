# liangongbao

## 批量答题抽奖

exe文件直接运行，不需要python环境

在这里[下载](https://github.com/vivishow/liangongbao/releases/tag/v1.0.0)

下载 [lgb.rar](https://github.com/vivishow/liangongbao/releases/download/v1.0.0/lgb.rar)
1. 解压在一个文件夹内。
2. 运行添加用户，用户名只作为区分用户使用.将所有用户扫码登陆后，会自动生成文件名为 userlist.json 的文件.也可以按照格式新建填入用户信息.
3. 双击答题程序，根据提示操作.

   需配合最新题库使用
   ps：试用版将于6-8到期

## 更新

题目有json和csv供大家自行选择
2023-06-05 15:00 更新题库 共148题

## 安装

1. 首先需要python3环境,官网下载<https://www.python.org/downloads/>

2. 安装mitmproxy

   `pip3 install mitmproxy`

---

新手直接下载这个和代码文件

​	mitmproxy官网 https://mitmproxy.org/ 下载安装程序安装.

这里要感谢[@8188](https://github.com/8188)同学的提醒

## 使用

1. 进入文件夹, 在空白处按住shift键再按鼠标右键,在此处打开cmd或者powershell.

2. 启动脚本

   `mitmdump -s aqy.py -p 8888 -q`

3. 打开手机进入无线网设置代理,IP设为运行脚本机器的IP地址,端口设为8888,也可以根据需要进行修改.

4. 浏览器打开 <mitm.it> 下载证书安装.

5. 新建文件夹 改名字为 *answer* 把题库文件 *answerdict.json*放到*answer*文件夹下.



## 视频教程

视频教程已出, B站[点我](https://www.bilibili.com/video/BV1rY411K7VH?share_source=copy_web). 

欢迎进群讨论qq群:217335772


## 说明

配合最新题库更佳!

仅供练功房使用.


## 赞赏

觉得不错的话,请我喝杯咖啡吧.![DONATE](./donate.jpg)