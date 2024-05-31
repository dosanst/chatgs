import socket  
  
HOST = '127.0.0.1'  # 连接到服务器的IP地址  
PORT = 65432        # 连接到服务器的端口  
  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
    s.connect((HOST, PORT))  
  
    while True:  
        message = input('Enter message: ')  
        if message.lower() == 'exit':  
            break  
        s.sendall(message.encode())  
        data = s.recv(1024)  
        print(f'Received: {data.decode()}')  
  
print('Closing connection...')
