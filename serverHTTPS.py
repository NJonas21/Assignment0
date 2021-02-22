import socket


serverName = socket.gethostname()
server_ip = socket.gethostbyname(serverName)

server_port = 50001

print(f"name: {serverName}")
print(f"IP: {server_ip}")


# TODO: Add a Map/dictionary with recognized header commands that aren't GET, PUT etc.
# Like "Connection: close" or User-agent: Mozilla/5.0
# Need to include data size as well (This will not need to be exact)
# Ajit said there needed to be at least 5 map categories.

# TODO: Add a method for each HTTP request command
# (GET, PUT, POST, DELETE, HEAD)

server_addr = (server_ip, server_port) # Remember it is a tuple you dummy

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket

# SOCK_STREAM = Stream of bytes

server_socket.bind(server_addr) # Bind to address

print("Listening for clients")

server_socket.listen(5) # Listen for clients

conn, address = server_socket.accept() # Receiving tuple with (socket, address)

print("Client Accepted!")

# Exercise : Learn how to use flags
header = conn.recv(1024).decode("utf-8") # Specify size in Bytes
# Also make sure the decoding is the same as the encoding

commands = header.split("\n") # split by normal \n character

commandsLen = len(commands)

for i in range(1, commandsLen, 1):
    print(commands[i])
    # TODO: Check for if all commands other than primary header in the map
    # If even one is missing, cancel the request and return a bad response
    # to the client
    # Also find the size of the data here

#print(message)

conn.close()

server_socket.close()
