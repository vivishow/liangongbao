# 题库更新

因之前群内出现题库被盗用的情况,现只更新hash版题库,需配合新版本使用.
更新于 2023-06-10 14:00 共287题

# 自动版

## 批量答题抽奖

exe文件直接运行，不需要python环境

~~在这里[下载](https://github.com/vivishow/liangongbao/releases/tag/v1.1.0)~~

~~下载 [BatchAnswer V1.1.0.rar](https://github.com/vivishow/liangongbao/releases/download/v1.1.0/BatchAnswer.rar)~~
- 解压在一个文件夹内。仔细阅读使用教程
- 需配合最新题库使用

~~ps：已过期~~

### 更新内容
- 添加用户信息可追加,不再完全覆盖
- 日志显示用户编号
- 答题时增加题目类型显示
- 修复登陆失败找不到用户编号
- 修复答错题不能继续
# 手动防滑版
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