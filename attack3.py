# 获取获取本机ip
import socket
import threading
import os
hn=socket.gethostname()
ip=socket.gethostbyname(hn)
def testip(ip):
    c=f"ping {ip}"
    ret=os.system(c)
    print(ret)
# testip(ip)
# 发起tcp连接
def tcpattack(ip):
    #第一步：创建一个socket
    sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #第二步：建立连接
    try:
        sc.connect((ip,8080))
        #第三步：发送数据
        sc.send(b'hello World!')
        #第三步：接收数据
        date=sc.recv(1024)
        print(date.decode('utf-8'))
    except:
        return 0
# 发起UDP连接
def udpattack(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        # 创建一个基于UDP的socket对象
    s.sendto('hello!'.encode(), (ip,80))            # 向指定服务器与端口号发送内容
    try: 
        s.recv(1024)                     
        s.close()
    except:
        return 0
def scan_poort(port,ip):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        statu=s.connect_ex((ip,port))
        if statu==0:
            print(port,'is open')
    except:
        return 0
# testip(ip)
# # udpattack(ip)
# tcpattack(ip)
for i in range(80,800):
    threading.Thread(target=scan_poort,args=(i,ip,)).start()


