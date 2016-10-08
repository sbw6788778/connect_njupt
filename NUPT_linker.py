import requests
import re
import os
import subprocess
import time
def canConnect():
        fnull = open(os.devnull, 'w')
        #设置子进程判断是否联网
        result = subprocess.call('ping www.baidu.com', shell = True, stdout = fnull, stderr = fnull)
        fnull.close()
        if result:
            return False
        else:
            return True
def continue_link():
        print(current_time()+'网络断开正在重新连接（请确保已经连接上NJUPT）')
        link()
def link():
        url='http://192.168.168.168/0.htm'
        data={'DDDDD':'121101502083600','upass':'040213','0MKKey':'','v6ip':''}
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36','Host':'192.168.168.168','Origin':'http://192.168.168.168','Referer':'http://192.168.168.168/0.htm'}
        html=requests.post(url,data,headers=headers)
        html=html.content.decode('gbk')
        r=re.compile('<form name="f1" method="post" action="">.*?<div id="info" style="height:100px; padding-top:30px;" class="font1">\r\n\t\t\t\t(.*?)<br>.*?</div>.*?</form>',re.S)
        htm=re.findall(r,html)
        print (htm)
def current_time():
        #strftime将时间格式化显示,并返回会str类型，localtime返回本地时间
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
while 1:
        can_Connect=canConnect()
        if can_Connect==False:
                continue_link()
        else:
                print(current_time()+'网络连接正常')
        time.sleep(10)
