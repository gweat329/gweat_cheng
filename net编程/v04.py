import socket

def tcp_srv():
    # 1. 建立socket负责具体通信，这个socket其实只负责接受对方的请求，正真通信的是链接后
    # 需要用到两个参数
    # AF-INET: 含义用udp一致
    # SOCK_STREAM: 表明是使用的tcp进行通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定端口和地址
    # 此地址信息是一个元组内容，元组两部分，第一部分为字符串，代表ip，第二部分为端口
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)
    # 3. 监听接入的访问socket
    sock.listen()

    while True:
        pass
