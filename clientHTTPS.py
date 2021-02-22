import socket
import time

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

splitMsg = message.split("\n\n") # Split header and data by \n\n

header = splitMsg[0]
data = splitMsg[1]

client_socket.send(header.encode('utf-8')) # Turns message into a byte string
# Send the header

time.sleep(2) # give the server some time to process info

# TODO: Create check for server response on whether request was valid or not
# If request was valid, send data.

client_socket.close()
