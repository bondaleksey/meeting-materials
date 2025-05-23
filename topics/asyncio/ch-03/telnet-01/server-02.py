import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 8008))
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f"Connection request received from {client_address}")

    buffer = b""

    while buffer[-2:] != b"\r\n":
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f"Received data: {data!r}!")
            buffer = buffer + data

    print(f"All data received: {buffer!r}")
finally:
    print("Closing server socket...")
    server_socket.close()
    print("Server socket closed.")
