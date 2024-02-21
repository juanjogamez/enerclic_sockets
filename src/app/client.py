"""
Coded by juanjogamez

client.py
"""
import socket
import threading


def receiving_handler(client_socket):
    """
    This function takes care of the reception of messages while client execution
    :param client_socket: socker which data will be received from
    :return: void
    """
    while True:
        # recv() is a blocking call: blocks code execution until data is received or connection is closed
        data = client_socket.recv(1024)
        if not data:
            break
        response = data.decode('utf-8')
        print(f"\nMessage received {response}")
        print("Enter your message: ")


def main():
    # Socket object instance: (AF_INET -> IPv4, SOCK_STREAM -> TCP Socket)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '172.18.0.10'  # Server IP
    port = 33333        # Server Port
    client_socket.connect((host, port))  # Establishing connection
    rec_handler = threading.Thread(target=receiving_handler, args=(client_socket,))  # Establishing thread
    rec_handler.start()  # Once connection is established, receiving handler will take care of receiving messages

    # Infinite loop to ask user for messages to send
    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode('utf-8'))  # Sending complete encoded message


if __name__ == "__main__":
    main()
