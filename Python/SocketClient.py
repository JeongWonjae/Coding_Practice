import socket

serverIP="192.168.11.104"
size=1024
port=4444

server_addr=(serverIP, port)
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_addr)
client_socket.send('im client'.encode("utf-8"))
if (client_socket.recv(size)):
    msg=client_socket.recv(size)
    msg=msg.decode("utf-8")
    print("(+) recv data is {}".format(msg))

client_socket.close()