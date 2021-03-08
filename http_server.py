# Authors: Nick Jonas, Bram Dedrick, Chen Xi
import socket
import time
import os
import datetime


def get(request):
    """Fucntion to replicate GET method"""
    if os.path.exists(request[1]):
        f = open(request[1], "r")
        data = f.read()
        f.close()
        return "200 OK", data
    data = None
    return "404 Not Found", data
# End of GET()


def post(request, parameters):
    """Function to replicate POST method"""
    if os.path.exists(request[1]):
        f = open(request[1], "a")
        f.write("\n" + parameters)
        f.close()
        f = open(request[1], "r")
        data = f.read()
        f.close()
        return "200 OK", data
    return "404 Not Found", None
# End of Post()


def put(request, parameters):
    """Function to replicate PUT method"""
    if not os.path.exists(request[1]):
        return "400 Bad Request", None
    f = open(request[1], 'w')
    f.write(parameters)
    f.close()
    f = open(request[1], 'r')
    data = f.read()
    f.close()
    return "200 OK", data
# End of PUT()


def delete(request):
    """Function to replicate DELETE method"""
    if os.path.exists(request[1]):
        os.remove(request[1])
        return "200 OK", "File deleted successfully."
    return "404 Not Found", None
# End of DELETE()


def head(request):
    """Function to replicate HEAD method"""
    if os.path.exists(request[1]):
        return "200 OK"
    return "404 Not Found"
# End of HEAD()


def main():
    """Main function"""

    # Generate essential information
    server_name = socket.gethostname()
    server_ip = socket.gethostbyname(server_name)

    print(server_ip)
    server_port = 50001

    # Server fields for header
    server_fields = {"Connection": "close", "Server": "Windows 10",
                     "Date": str(datetime.datetime.now()), "Content-Length": None, "Content-Type": "text"}

    server_addr = (server_ip, server_port)  # Remember it is a tuple you dummy

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create server socket

    # SOCK_STREAM = Stream of bytes

    server_socket.bind(server_addr)  # Bind to address

    server_socket.listen(5)  # Listen for clients

    client_conn, client_address = server_socket.accept()
    # Receiving tuple with (socket, address)

    connection_bool = True

    while connection_bool:  # While loop
        # Receive the buffer size needed
        buf_size = int(client_conn.recv(4).decode("utf-8"))  # Specify size in Bytes
        # Also make sure the decoding is the same as the encoding
        if buf_size != 2:
            client_conn.send("received".encode("utf-8"))  # Send a confirmation message

            time.sleep(1)

            request = client_conn.recv(buf_size).decode("utf-8")  # Now recieve the request

            header, data = request.split("\n\n")  # Split by normal \n character

            header_split = header.split("\n")

            response_list = []  # Creates empty list to add header lines

            method = header_split[0].split(" ")  # Get the first line of header
            version = method[2].split("/")  # Find the version
            version_num = float(version[1])

            if version_num >= 1.0:  # Checking to see if the version is valid
                if method[0] == "GET":  # Checking each method for valid method, if true then execute it
                    status_code, entity_body = get(method)
                elif method[0] == "PUT":
                    status_code, entity_body = put(method, data)
                elif method[0] == "POST":
                    status_code, entity_body = post(method, data)
                elif method[0] == "HEAD":
                    status_code = head(method)
                    entity_body = None
                elif method[0] == "DELETE":
                    status_code, entity_body = delete(method)
                else:
                    status_code = "400 Bad Request"
                    entity_body = None
            else:
                status_code = "505 HTTP Version Not Supported"
                entity_body = None

            response_list.append(status_code)

            if status_code == "200 OK":
                for i in header_split[1:]:
                    header_field = i.split(": ")
                    if header_field[0] == "Content-Length":  # Figure out content length
                        if entity_body is not None:
                            response_list.append(f"Content-Length: {len(entity_body.encode('utf-8'))}")
                        else:
                            response_list.append(f"Content-Length: 0")
                    else:  # If client mentioned the header_field, send back the server equivalent if it has it
                        if header_field[0] in server_fields.keys():
                            response_list.append(f"{header_field[0]}: {server_fields[header_field[0]]}")

            response_message = "HTTP/"  # creates response string
            response_message += str(version_num)  # adds version number to that string
            response_message += " "

            for response_line in response_list:  # create the response string
                response_message += f"{response_line} \n"

            if entity_body is not None:
                response_message += "\n" + entity_body  # Add the data

            response_enc = response_message.encode("utf-8")  # encode the response
            response_size = len(response_enc)  # Get size of response

            response_size_str = str(response_size)

            client_conn.send(response_size_str.encode("utf-8"))  # Send the size of response for the client

            time.sleep(1)  # give client time to process

            client_conn.send(response_enc)  # Send response
        else:
            break

    client_conn.close()  # Close connections

    server_socket.close()
# End of main()


if __name__ == "__main__":
    main()
