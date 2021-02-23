import socket
import time


# TODO: Put everything in a main function

clientName = socket.gethostname()
client_ip = socket.gethostbyname(clientName)

client_port = 50002

server_ip = "10.104.65.5"
server_port = 50001

server_addr = (server_ip, server_port)

client_addr = (client_ip, client_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_addr)

#message = input("Type a HTTP request for the server: ") # Header + data

message = f"GET webserver/a.txt HTTP/1.1\nConnection: closed\nhost: {clientName}\n\nGenerated data here"

encodeMsg = message.encode("utf-8")

bufsize = len(encodeMsg)

#Send the initial byte size for buffer
client_socket.send(str(bufsize).encode("utf-8")) # Turns message into a byte string

time.sleep(1) # give the server some time to process info

conf = client_socket.recv(8)

client_socket.send(encodeMsg)

# TODO: Create check for server response on whether request was valid or not
# If request was valid, send data.

client_socket.close()
