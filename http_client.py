import socket
import time


def main():
    """Main function"""
    clientName = socket.gethostname()
    client_ip = socket.gethostbyname(clientName)

    client_port = 50002 # Client port

    server_ip = "192.168.56.1" # Need Server ip
    server_port = 50001 # Server port

    server_addr = (server_ip, server_port)

    client_addr = (client_ip, client_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(server_addr)

    #message = input("Type a HTTP request for the server: ") # Header + data

    message = f"POST webserver/a.txt HTTP/1.1\nConnection: closed\nhost: {clientName}\n\nClient's Parameters"

    encodeMsg = message.encode("utf-8")

    bufsize = len(encodeMsg)

    #Send the initial byte size for buffer
    client_socket.send(str(bufsize).encode("utf-8")) # Turns message into a byte string

    time.sleep(1) # give the server some time to process info

    conf = client_socket.recv(8) # Receiving confirmation from the server

    client_socket.send(encodeMsg) # Sending the message

    time.sleep(1) # waiting for server to process

    responseSize = int(client_socket.recv(4).decode("utf-8")) # Receive server response size

    response = client_socket.recv(responseSize).decode("utf-8") # Receiving the actual response

    print(response) # Print the response

    client_socket.close()
#End of main()


if __name__ == "__main__":
    main()
