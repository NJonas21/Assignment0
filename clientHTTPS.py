import socket

clientName = socket.gethostname()
client_ip = socket.gethostbyname(clientName)

client_port = 50002

server_ip = "10.104.65.5"
server_port = 50001

server_addr = (server_ip, server_port)

client_addr = (client_ip, client_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_addr)

message = input("Type a HTTP request for the server: ") # Header + data

client_socket.send(message.encode('utf-8')) # Turns message into a byte string

client_socket.close()
