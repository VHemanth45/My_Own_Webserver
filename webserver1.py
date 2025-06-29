import socket

HOST, PORT = '', 8888

#creates a TCP/IP socket and setting the TCP protocol
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sets the socket options to allow reuse of the address
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind the socket to the address and port
listen_socket.bind((HOST, PORT))
#puts the socket into listening mode
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
