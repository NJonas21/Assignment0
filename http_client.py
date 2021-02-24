# Authors: Nick Jonas, Bram Dedrick, Chen Xi
import socket
import time


def main():
    """Main function"""
    clientName = socket.gethostname()
    client_ip = socket.gethostbyname(clientName)

    client_port = 50002 # Client port

    server_ip = "10.104.65.5" # Need Server ip
    server_port = 50001 # Server port

    server_addr = (server_ip, server_port)

    client_addr = (client_ip, client_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(server_addr)

    #message = input("Type a HTTP request for the server: ") # Header + data

    pre_made_messages = ["DELETE webserver/deleteme.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nContent-Length: 1024\nDate: \nServer: \n\n",
    "GET webserver/404notfound.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nContent-Length: 1024\nDate: \nServer: \n\n",
    "PUT webserver/a.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nContent-Length: 1024\nDate: \nServer: \n\nthis file exists right?",
    "POST webserver/a.txt HTTP/0.9\nConnection: open\nConnection-Type: txt\nContent-Length: 1024\nDate: \nServer: \n\nversion check.",
    "GET webserver/a.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nDate: \nServer: \n\n",
    "GOT webserver/a.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nDate: \nServer: \n\n",
    "GET webserver/a.txt HTTP/0.1\nConnection: open\nConnection-Type: txt\nDate: \nServer: \n\n",
    "POST webserver/a.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nContent-Length: \nDate: \nServer: \n\nPut this in a.txt",
    "PUT webserver/c.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nContent-Length: \nDate: \nServer: \n\nThis will be in a new file.",
    "HEAD webserver/a.txt HTTP/1.1\nConnection: open\nConnection-Type: txt\nDate: \nServer: \n\n", "-1"]

    for message in pre_made_messages:
        encodeMsg = message.encode("utf-8")

        bufsize = len(encodeMsg)

        #Send the initial byte size for buffer
        client_socket.send(str(bufsize).encode("utf-8")) # Turns message into a byte string

        time.sleep(1) # give the server some time to process info

        conf = client_socket.recv(8) # Receiving confirmation from the server

        client_socket.send(encodeMsg) # Sending the message

        #time.sleep(1) # waiting for server to process


        if message != "-1":
            responseSize = client_socket.recv(4).decode("utf-8") # Receive server response size
            responseSizeStr = str(responseSize)
            responseSizeInt = int(responseSizeStr)
            response = client_socket.recv(responseSizeInt).decode("utf-8") # Receiving the actual response

            print(response + "\n") # Print the response
            time.sleep(2)

    client_socket.close()
#End of main()


if __name__ == "__main__":
    main()
