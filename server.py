import socket  
  
HOST = '127.0.0.1'  # 监听本地IP地址  
PORT = 65432        # 监听端口  
  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
    s.bind((HOST, PORT))  
    s.listen()  
    print(f'Server listening on {HOST}:{PORT}...')  
  
    clients = {}  
  
    def broadcast(message):  
        for client_socket in clients:  
            #if client_socket != s.client_address:  # 可能需要添加一个条件来避免向发送者自己发送消息  
            client_socket.sendall(message)  # 直接发送bytes数据
  
    while True:  
        client_socket, client_address = s.accept()  
        print(f'Accepted connection from {client_address}')  
  
        clients[client_socket] = client_address  
  
        try:  
            while True:  
                data = client_socket.recv(1024)  
                if not data:  
                    break  
                message = data.decode()  # 将bytes解码为字符串（如果需要的话）  
                print(f'Received "{message}" from {client_address}')  
                broadcast(data)  # 直接发送原始的bytes数据
        finally:  
            print(f'Closing connection to {client_address}')  
            client_socket.close()  
            del clients[client_socket]
