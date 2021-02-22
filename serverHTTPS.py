import socket




# TODO: Add a Map/dictionary with recognized header commands that aren't GET, PUT etc.
# Like "Connection: close" or User-agent: Mozilla/5.0
# Need to include data size as well (This will not need to be exact)
# Ajit said there needed to be at least 5 map categories.

# TODO: Add a method for each HTTP request command
# (GET, PUT, POST, DELETE, HEAD)

def GET():
    #Insert function for GET method here
    return None

def POST():
    #Insert function for POST method here
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

clinet_conn, client_address = server_socket.accept() # Receiving tuple with (socket, address)

print("Client Accepted!")

# Exercise : Learn how to use flags
header = client_conn.recv(1024).decode("utf-8") # Specify size in Bytes
# Also make sure the decoding is the same as the encoding

commands = header.split("\n") # split by normal \n character


for i in commands:
    if ":" is not in i:
        cmdSplit = i.split(" ")
        if cmdSplit[0] == "GET":
            #GET(cmdSplit, client_conn)
        elif cmdSplit[0] == "POST":
            #POST(cmdSplit, client_conn)
        elif cmdSplit[0] == "PUT":
            #PUT(cmdSplit, client_conn)
        elif cmdSplit[0] == "HEAD":
            #HEAD(cmdSplit, client_conn)
        else:
            #DELETE(cmdSplit, client_conn)
    else:
        print(i)
    # TODO: Check for if all commands other than primary header in the map
    # If even one is missing, cancel the request and return a bad response
    # to the client
    # Also find the size of the data here

#print(message)

conn.close()

server_socket.close()
