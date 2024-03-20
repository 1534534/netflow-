#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil
import speedtest
import time


def monitor_network():
    while True:
        # 获取系统资源利用情况
        disk_usage = psutil.disk_usage('/')
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        # 测量网络速度
        st = speedtest.Speedtest()
        download_speed = st.download() / 1024 / 1024  # 转换为 Mbps
        upload_speed = st.upload() / 1024 / 1024  # 转换为 Mbps

        # 打印监控信息
        print(f'磁盘使用率：{disk_usage.percent}%')
        print(f'磁盘总量：{disk_usage.total / 1024 ** 3:.2f}GB')
        print(f'磁盘剩余量：{disk_usage.free / 1024 ** 3:.2f}GB')
        print(f'磁盘已使用量：{disk_usage.used / 1024 ** 3:.2f}GB')
        print(f"CPU 使用率: {cpu_usage}%")
        print(f"内存使用率: {memory_usage}%")
        print(f"下载速度: {download_speed:.2f} Mbps")
        print(f"上传速度: {upload_speed:.2f} Mbps")
        print("-" * 30)

        # 每隔一段时间进行监控
        time.sleep(300)  # 每5分钟监控一次


if __name__ == "__main__":
    monitor_network()
