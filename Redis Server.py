import socket
import threading
import time

# A simple in-memory key-value store for the Redis-like server
kv_store = {}

# RESP serialization and deserialization functions
def serialize(data):
    """Serialize Python data into RESP format."""
    if isinstance(data, str):
        return f"+{data}\r\n"
    elif isinstance(data, int):
        return f":{data}\r\n"
    elif isinstance(data, list):
        # Bulk Strings for arrays
        serialized_list = "".join(serialize(item) for item in data)
        return f"*{len(data)}\r\n{serialized_list}"
    elif data is None:
        return "$-1\r\n"  # Null Bulk String
    else:
        return f"-Invalid data type\r\n"

def deserialize(data):
    """Deserialize RESP data into Python format."""
    if data.startswith("+"):
        return data[1:].strip()
    elif data.startswith(":"):
        return int(data[1:].strip())
    elif data.startswith("$"):
        length = int(data[1:].strip())
        if length == -1:
            return None
        return data.split("\r\n", 2)[1]
    elif data.startswith("*"):
        count = int(data[1:].strip())
        elements = []
        current_data = data[data.index("\r\n") + 2 :]
        for _ in range(count):
            element = deserialize(current_data)
            elements.append(element)
            current_data = current_data[current_data.index("\r\n") + 2 :]
        return elements
    else:
        return f"-Error: Unsupported RESP type"

# Command handling
def handle_command(command):
    """Handles Redis-like commands such as PING, ECHO, SET, GET."""
    global kv_store

    if command[0].lower() == "ping":
        return serialize("PONG")
    elif command[0].lower() == "echo":
        return serialize(command[1])
    elif command[0].lower() == "set":
        if len(command) != 3:
            return serialize("Error: SET requires 2 arguments")
        kv_store[command[1]] = command[2]
        return serialize("OK")
    elif command[0].lower() == "get":
        if len(command) != 2:
            return serialize("Error: GET requires 1 argument")
        return serialize(kv_store.get(command[1], None))
    else:
        return serialize(f"-Error: Unknown command {command[0]}")

# Client handler to process incoming commands
def client_handler(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            command = deserialize(data)
            if isinstance(command, list):
                response = handle_command(command)
                client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

# Main Redis server
def start_redis_server(host="127.0.0.1", port=6379):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Redis server is running on {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_redis_server()
