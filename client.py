import socket
import logging


def connect() -> socket:
    logger.info("Creating client info...")
    client_info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info("Connecting to a server...")
    client_info.connect((ADDRESS, PORT))
    logger.info(f"Connected to {ADDRESS}:{PORT}")
    return client_info


def run(message: str):
    message_length = str(len(message)).encode(FORMAT)
    message_length += b' ' * (HEADER - len(message_length))
    logger.info(f"Sending message: {message}")
    client.send(message_length)
    client.send(message.encode(FORMAT))


if __name__ == "__main__":
    logging.basicConfig()
    logger = logging.getLogger("Client")
    logger.setLevel(logging.INFO)

    ADDRESS = "192.168.1.19"
    PORT = 5050
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"

    client = connect()
    try:
        run(message="Ala ma kota")
    finally:
        run(message=DISCONNECT_MESSAGE)
