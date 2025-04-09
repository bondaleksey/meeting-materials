import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 8008))
server_socket.listen()

connections = []

try:
    while True:
        connection, client_address = server_socket.accept()
        print(f"Connection request received from {client_address}")
        connections.append(connection)

        for con in connections:
            buffer = b""

            while buffer[-2:] != b"\r\n":
                data = con.recv(2)
                if not data:
                    break
                else:
                    print(f"Received data: {data}!")
                    buffer = buffer + data

            print(f"All data received: {buffer}")
            con.send(b"HTTP/1.0 200 OK\r\n\r\n")
            con.send(buffer)
finally:
    print("Closing server socket...")
    server_socket.close()
    print("Server socket closed.")
