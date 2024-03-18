from django.test import TestCase

# Create your tests here.
import datetime
import os
import psutil
from tabulate import tabulate
import time
import pymysql

class NetworkTrafficMonitor:
    """
    网络流量监视工具
    """
    def __init__(self):
        print("网络流量监视器启动..........")

    def get_network_bytes(self):
        """
        获取当前端口收发字节数
        :return:当前各个端口的收发字节数
        """
        network_io = psutil.net_io_counters(pernic=True)
        bytes_now = {}
        for interface, io in network_io.items():
            bytes_now[interface] = {'上传字节数': io.bytes_sent, '下载字节数': io.bytes_recv}
        return bytes_now
    def format_speed(self, speed):
        """
        获取直观的网速格式
        :param speed: 网速 Byte/s
        :return: 格式化网速
        """
        if speed < 1024:
            return f"{speed} B/s"
        elif speed < 1048576:
            return f"{speed / 1024:.2f} KB/s"
        else:
            return f"{speed / 1048576:.2f} MB/s"

    def format_netdata(self, da):
        """
        获取直观的流量格式
        :param da: 字节数
        :return: 格式化字节数
        """
        if da < 1024:
            return f"{da} B"
        elif da < 1048576:
            return f"{da / 1024:.2f} KB"
        elif da < 1073741824:
            return f"{da / 1048576:.2f} MB"
        else:
            return f"{da / 1073741824:.2f} GB"

    def cmd_mode(self):
        """
        cmd模式下的监视器
        :return:
        """

        last_speed = self.get_network_bytes()  # 获取一次当前收发字节数，用于计算网速
        raw_speed = self.get_network_bytes()  # 获取一次当前收发字节数，用于累积计算流量

        # 创建初始字节数字典用于运算
        raw = {}
        for interface, bytes1 in raw_speed.items():
            raw[interface] = [bytes1['上传字节数'], bytes1['下载字节数']]
        while True:

            network_speeds = self.get_network_bytes()  # 获取一次当前收发字节数

            # 创建上一次字节数字典用于运算
            last = {}
            for interface, bytes1 in last_speed.items():
                last[interface] = [bytes1['上传字节数'], bytes1['下载字节数']]

            data = []  # 用于显示数据的列表
            for interface, bytes1 in network_speeds.items():
                data.append([interface, self.format_speed(bytes1['上传字节数'] - last[interface][0]),
                             self.format_speed(bytes1['下载字节数'] - last[interface][1]),
                             self.format_netdata(bytes1['上传字节数'] - raw[interface][0]),
                             self.format_netdata(bytes1['下载字节数'] - raw[interface][1])])
            # 用tabulate库中tabulate函数生成表格对象
            headers = ["接口", "上传速率", "下载速率", "累积上传", "累积下载"]
            table = tabulate(data, headers, tablefmt="grid")
            for item in data:
                for i in range(0,5):
                    item[i] =headers[i]+":"+ item[i]
            list = []
            for item in data[3]:
                list.append(item.split(':')[-1])
            print(list)
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                passwd="111111",
                db="mysql",
                charset="gbk",

            )
            cursor = conn.cursor()
            sql = "insert into b_netdata(port, upload_speed,download_speed,upload_all,download_all,time) values(%s, %s, %s, %s,%s,%s)"
            port = list[0]
            upload_speed = list[1]
            download_speed = list[2]
            upload_all = list[3]
            download_all = list[4]
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(sql, (port, upload_speed, download_speed, upload_all, download_all,time1))
            time.sleep(5)  # 等待一秒
            conn.commit()
            conn.close()

if __name__ == '__main__':
    monitor = NetworkTrafficMonitor()
    monitor.cmd_mode()