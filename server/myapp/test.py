
#先下载psutil库:pip install psutil

import psutil
import os,datetime
def main():
        print ("电脑的开机时间",)
        #调用psutil.boot_time()函数返回开机的时间戳
        dt =  datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d,%H:%M:%S")
        #返回一个datetime对象
        print(dt.strftime("%Y-%m-%d,%H:%M:%S"))
if __name__=="__main__":
        main()