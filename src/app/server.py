"""
Coded by juanjogamez

server.py
"""
import socket
import threading
import datetime

clients_list = []    # Global tuple-list variable to keep track of established sockets


def handle_client(client_socket, client_address):
    """ This function handles a client connection to the server (considering threading)
    :param client_address:
    :param client_socket:
    :return: void
    """
    while True:
        # recv() is a blocking call: blocks code execution until data is received or connection is closed
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        # Saving message in logs file
        with open("/logs/messages.log", "a") as log_file:
            log_file.write(f"Received message from {client_address}: {message} at {datetime.datetime.utcnow()}\n")
        message = "from " + str(client_address) + ':' + message
        for conn in clients_list:
            if conn[1] != client_address:
                # Sending data to the opposite client (since we consider only 2 for current scenario)
                conn[0].sendall(message.encode('utf-8'))
    client_socket.close()
    clients_list.remove((client_socket, client_address))  # Removing client tuple from local variable


def main():
    # Socket object instance: (AF_INET -> IPv4, SOCK_STREAM -> TCP Socket)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '172.18.0.10'  # Server IP
    port = 33333        # Server Port
    server_socket.bind((host, port))  # Linking socket to host, port
    server_socket.listen(3)     # 3 indicates the maximum number of connections on wait
    print(f"Server listening on {host}:{port}")

    while True:
        # accept() is a blocking call: blocks code execution until a connection is required
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # Establishing thread:
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()
        clients_list.append((client_socket, client_address))    # Adding connection to global list variable


if __name__ == "__main__":
    main()
