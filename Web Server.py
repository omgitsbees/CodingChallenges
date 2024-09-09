import socket
import threading
import os

# Configurations
HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Port to listen on (default HTTP port is 80, but we'll use 8080 for testing)
WWW_DIR = os.path.join(os.getcwd(), "www")  # Serve files from a www directory

# Ensure the www directory exists
if not os.path.exists(WWW_DIR):
    os.mkdir(WWW_DIR)
    with open(os.path.join(WWW_DIR, "index.html"), "w") as f:
        f.write("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Simple Web Page</title>
        </head>
        <body>
            <h1>Test Web Page</h1>
            <p>My web server served this page!</p>
        </body>
        </html>
        """)

# Function to handle client connections
def handle_client_connection(client_socket):
    try:
        request = client_socket.recv(1024).decode('utf-8')
        if request:
            # Extract the first line of the request
            request_line = request.splitlines()[0]
            print(f"Received request: {request_line}")
            
            # Parse the request line
            method, path, _ = request_line.split(' ')
            
            # Only handle GET requests
            if method == 'GET':
                if path == '/':
                    path = '/index.html'

                # Create full path to requested file
                file_path = os.path.join(WWW_DIR, path.lstrip('/'))

                if os.path.exists(file_path) and file_path.startswith(WWW_DIR):
                    # Serve the file
                    with open(file_path, 'r') as f:
                        response_body = f.read()
                    
                    # Prepare response
                    response_headers = "HTTP/1.1 200 OK\r\n\r\n"
                    client_socket.sendall(response_headers.encode('utf-8') + response_body.encode('utf-8'))
                else:
                    # File not found
                    response = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
                    client_socket.sendall(response.encode('utf-8'))
            else:
                # Method not allowed
                response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n<h1>405 Method Not Allowed</h1>"
                client_socket.sendall(response.encode('utf-8'))
        client_socket.close()
    except Exception as e:
        print(f"Error handling request: {e}")
        client_socket.close()

# Function to start the server and listen for connections
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Max number of queued connections
    print(f"Serving HTTP on {HOST} port {PORT} (http://{HOST}:{PORT}/) ...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        
        # Handle client connections in a new thread
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    start_server()
