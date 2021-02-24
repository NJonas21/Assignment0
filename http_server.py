import socket
import time
import os



# TODO: Add a Map/dictionary with recognized header commands that aren't GET, PUT etc.
# Like "Connection: close" or User-agent: Mozilla/5.0
# Need to include data size as well (This will not need to be exact)
# Ajit said there needed to be at least 5 map categories.

# TODO: Add a method for each HTTP request command
# (GET, PUT, POST, DELETE, HEAD)

def GET():

    return None

def POST():

    return None

def PUT():
    #Insert function for PUT method here
    return None

def DELETE():
    #Insert function for DELETE method here
    return None

def HEAD():
    #Insert function for HEAD method here
    return None

def headerFields(headerSplit):
    return None


# TODO: Put everything in a main function

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

client_conn, client_address = server_socket.accept()
# Receiving tuple with (socket, address)

print("Client Accepted!")

# Receive the bufsize needed
bufsize = int(client_conn.recv(4).decode("utf-8")) # Specify size in Bytes
# Also make sure the decoding is the same as the encoding

client_conn.send("received".encode("utf-8"))

time.sleep(1)

request = client_conn.recv(bufsize).decode("utf-8") # Now recieve the request

print(f"request = \n{request}")

header, data = request.split("\n\n") # split by normal \n character

headerSplit = header.split("\n")

response = []


cmdSplit = headerSplit[0].split(" ")
version= cmdSplit[2].split("/")
versionNum = float(version[1])
cond1 = versionNum >= 1.0
cond2 = versionNum <= 2.0
cond3 = os.path.exists(cmdSplit[1]) == True

if cond1 and cond2:
    if cond3:
        if cmdSplit[0] == "GET":
            print("got")
        elif cmdSplit[0] == "PUT":
            print("put")
        elif cmdSplit[0] == "POST":
            print("post")
        elif cmdSplit[0] == "HEAD":
            print("head")
        else:
            print("delete")


for i in headerSplit[1:]:
    headerfield = i.split(": ")
    response.append(headerFields(headerfield))
    print(i)
    # TODO: Check for if all commands other than primary header in the map
    # If even one is missing, cancel the request and return a bad response
    # to the client
    # Also find the size of the data here

responseMessage = ""
for j in response:
    responseMessage += f"{response} \n"

print(responseMessage)
#TODO: Send Response message back to client with data attached

client_conn.close()

server_socket.close()
