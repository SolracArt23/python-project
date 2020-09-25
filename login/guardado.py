import socket
host=socket.gethostbyname(socket.gethostname())
puerto=1212
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,puerto))
while True:
    conn,add=server.accept()










