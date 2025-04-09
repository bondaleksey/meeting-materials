import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 8008))
server_socket.listen()

connection, client_address = server_socket.accept()
print(f"Connection request received from {client_address}")
