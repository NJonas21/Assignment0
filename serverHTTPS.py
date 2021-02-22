import socket


serverName = socket.gethostname()
server_ip = socket.gethostbyname(serverName)

server_port = 50001

print(f"name: {serverName}")
print(f"IP: {server_ip}")

server_addr = (server_ip, server_port) # Remember it is a tuple you dummy

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket

# SOCK_STREAM = Stream of bytes

server_socket.bind(server_addr) # Bind to address

print("Listening for clients")

server_socket.listen(5) # Listen for clients

conn, address = server_socket.accept() # Receiving tuple with (socket, address)

print("Client Accepted!")

# Exercise : Learn how to use flags
message = conn.recv(1024).decode("utf-8") # Specify size in Bytes
# Also make sure the decoding is the same as the encoding

print(message)

conn.close()

server_socket.close()
