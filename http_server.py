import socket
import time
import os
import datetime


def GET(request):
    """Fucntion to replicate GET method"""
    cond = os.path.exists(request[1]) == True
    if cond:
        f = open(request[1], "r")
        data = f.read()
        print(data)
        f.close()
        return "200 OK", data
    data = None
    return "404 Not Found", data
#End of GET()


def POST(request, parameters):
    """Function to replicate POST method"""
    cond = os.path.exists(request[1]) == True
    if cond:
        f = open(request[1], "a")
        f.write("\n" + parameters)
        f.close()
        f = open(request[1], "r")
        data = f.read()
        print(data)
        f.close()
        return "200 OK", data
    return "404 Not Found", None
#End of Post()


def PUT(request):
    """Function to replicate PUT method"""
    return "200 OK"
#End of PUT()

def DELETE(request):
    """Function to replicate DELETE method"""
    cond = os.path.exists(request[1]) == True
    if cond3:
        return "200 OK"
    return "404 Not Found"
#End of DELETE()


def HEAD(request):
    """Function to replicate HEAD method"""
    cond = os.path.exists(request[1]) == True
    if cond:
        return "200 OK"
    return "404 Not Found"
#End of HEAD()


def main():
    """Main function"""

    # Generate essential information
    serverName = socket.gethostname()
    server_ip = socket.gethostbyname(serverName)

    server_port = 50001

    print(f"name: {serverName}")
    print(f"IP: {server_ip}")

    # Server fields for header
    server_fields = {"Connection" : "close", "server" : "Windows 10",
                     "Date" : str(datetime.datetime.now()), "Content-Length": None, "Content-Type" : "text"}

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

    client_conn.send("received".encode("utf-8")) # Send a confirmation message

    time.sleep(1)

    request = client_conn.recv(bufsize).decode("utf-8") # Now recieve the request

    print(f"request = \n{request}")

    header, data = request.split("\n\n") # split by normal \n character

    headerSplit = header.split("\n")

    response = [] # Create empty list for formating response


    cmdSplit = headerSplit[0].split(" ") # Get the first line of header
    version= cmdSplit[2].split("/") # Find the version
    versionNum = float(version[1])
    cond = versionNum >= 1.0

    if cond: # Checking to see if the version is valid
        if cmdSplit[0] == "GET": # Checking each method for valid method, if true then execture it
            SerRespone, SerData = GET(cmdSplit)
        elif cmdSplit[0] == "PUT":
            SerResponse = PUT(cmdSplit)
            SerData = None
        elif cmdSplit[0] == "POST":
            SerResponse, SerData = POST(cmdSplit, data)
        elif cmdSplit[0] == "HEAD":
            SerResponse = HEAD(cmdSplit)
            SerData = None
        elif cmdSplit[0] == "DELETE":
            SerResponse = DELETE(cmdSplit)
            SerData = None
        else:
            SerResponse = "400 Bad Request"
    else:
        SerResponse = "505 HTTP version not supported"


    response.append(SerResponse)# Add the first line of response to message

    if SerResponse != "400 Bad Request" and SerResponse != "505 HTTP version not supported" and SerResponse != "404 Not Found":
        #Check if Server Response is 200 OK
        for i in headerSplit[1:]:
            headerfield = i.split(": ")
            if headerfield[0] == "Content-Length": # Figure out content length
                if SerData != None:
                    response.append(f"Content-Length: {SerData.encode('utf-8')}")
                else:
                    response.append(f"Content-Length: 0")
            else: # If client mentioned the headerfield, send back the server equivalent if it has it
                if headerfield[0] in server_fields.keys():
                    response.append(f"{headerfield[0]}: {server_fields[headerfield[0]]}")
                    

    responseMessage = "" # Empty string
    for j in response: # create the response string
        responseMessage += f"{j} \n"

    if SerData != None:
        responseMessage += "\n" + SerData # Add the data

    print(f"response = n\{responseMessage}") # Quick check

    responseEnc = responseMessage.encode("utf-8") # encode the response
    responseSize = str(len(responseEnc)) # Get size of response

    client_conn.send(responseSize.encode("utf-8")) # Send the size of response for the client

    time.sleep(1) # give client time to process

    client_conn.send(responseEnc) # Send response

    client_conn.close() # Close connections

    server_socket.close()
#End of main()

if __name__ == "__main__":
    main()
