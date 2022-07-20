import socket  # 创建TCP连接
from threading import Thread  # 多线程模块，进行多线程扫描
import time  # 时间模块，记录扫描所需时间


def main():
    target = input("ip或者域名:")
    start_time = time.time()
    s_time = time.ctime()
    print("[*] Start port scan at %s" % s_time)
    for port in range(1, 65536):  # 定义扫描的端口范围
        # 2、启动多线程运行PortScan函数
        t = Thread(target=portscan, args=(target, port))  # 创建线程对象
        t.start()  # 开始线程

    end_time = time.time()
    print("[*] All done in %.2f s" % (end_time - start_time))


def portscan(target, port):
    # 1、定义portscan函数，进行TCP端口扫描
    try:
        client = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
        client.settimeout(1)
        client.connect((target, port))  # 建立TCP连接
        print("[*] %s:%d端口开放" % (target, port))
        # 将开放端口记录到文件中
        with open(target + "-open_port.txt", "a") as f:
            f.write("%s:%d\n" % (target, port))

        client.close()
    except:
        pass  # 捕获异常


if __name__ == "__main__":
    main()
