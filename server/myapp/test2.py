# -*- coding: utf-8 -*-
import psutil
import datetime
import time


# 监控CPU信息
def cpu():
    cpu_per = int()  # 每秒cpu使用率，（1，true） 每一核cpu的每秒使用率； 36
    return psutil.cpu_percent(1)


# 监控内存信息
def mem():
    mem = psutil.virtual_memory()  # 查看内存信息:(total,available,percent,used,free)
    # print(mem)
    mem_total = int(mem[0] / 1024 / 1024)
    mem_used = int(mem[3] / 1024 / 1024)
    mem_per = int(mem[2])
    mem_info = {
        'mem_total': mem_total,
        'mem_used': mem_used,
        'mem_per': mem_per,
    }
    return mem_info
# 监控网络流量
def network():
    network = psutil.net_io_counters()  # 查看网络流量的信息；(bytes_sent, bytes_recv, packets_sent, packets_recv, errin, errout, dropin, dropout)
    # print(network)
    network_sent = int(psutil.net_io_counters()[0] / 8 / 1024)  # 每秒接受的kb
    network_recv = int(psutil.net_io_counters()[1] / 8 / 1024)
    network_info = {
        'network_sent': network_sent,
        'network_recv': network_recv
    }
    return network_info


# 间隔一定时间(10秒)，输出当前的CPU状态信息
def all_msg():
    msg = []
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # append之后是['2019-03-21 15:31:39']
    # now_time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')  # append之后是[datetime.datetime(2019, 3, 21, 15, 29, 42)]
    msg.append(now_time)  # 获取时间点 (f0)
    cpu_info = cpu()
    msg.append(cpu_info)  # cpu 使用率(f1),单位：%
    mem_info = mem()
    msg.append(mem_info['mem_per'])  # 内存使用率(f2),单位：%

    network_info = network()
    msg.append(network_info['network_sent'])  # 网络流量接收的量（MB）(f6)
    msg.append(network_info['network_recv'])  # 网络流量发送的量（MB） (f7)
    return msg





def main():
    cnt_times = 1
    while (1):
        msg = all_msg()
        print(msg)  # 实时打印每个十秒写入excel的数据。
        cnt_times += 1
        # 每隔10秒，统计一次当前计算机的使用情况。
        time.sleep(10)
        # 统计了20000次后跳出当前循环，统计的总共时间是：20000*10/3600 ~= 55.55
        if (cnt_times > 20000):
            break


main()

