import socket
import threading
import logging
import time


def client_handle(connection: socket, address: list):
    logger.info("New client connected")
    logger.info(f"CONNECTION: {connection}")
    logger.info(f"ADDRESS: {address}")

    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False
                logger.info(f"Client [{address}] disconnected.")
            else:
                logger.info(f"Client [{address}] -> Message: {message}")

    connection.close()
    threading.Thread(target=get_active_connections).start()


def get_active_connections():
    time.sleep(2)
    logger.info(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 2}")


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ADDRESS, PORT))

    logger.info(f"Starting server on {ADDRESS}...")
    server.listen()
    logger.info("Server started.")
    logger.info("Waiting for connections...")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=client_handle, args=(connection, address))
        thread.start()
        logger.info(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")


if __name__ == "__main__":
    logging.basicConfig()
    logger = logging.getLogger("Server")
    logger.setLevel(logging.INFO)

    ADDRESS = socket.gethostbyname(socket.gethostname())  # "192.168.1.19"
    PORT = 5050
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"

    start()
