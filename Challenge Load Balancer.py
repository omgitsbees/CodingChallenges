import socket
import threading
import requests
import time

class LoadBalancer:
    def __init__(self, servers, health_check_url="/", health_check_interval=10):
        self.servers = servers
        self.server_index = 0
        self.lock = threading.Lock()
        self.health_check_url = health_check_url
        self.health_check_interval = health_check_interval
        self.available_servers = servers.copy()
        self.start_health_check()

    def start_health_check(self):
        threading.Thread(target=self.health_check, daemon=True).start()

    def health_check(self):
        while True:
            for server in self.servers:
                try:
                    response = requests.get(f"http://{server}{self.health_check_url}")
                    if response.status_code == 200:
                        if server not in self.available_servers:
                            self.available_servers.append(server)
                    else:
                        if server in self.available_servers:
                            self.available_servers.remove(server)
                except requests.RequestException:
                    if server in self.available_servers:
                        self.available_servers.remove(server)
            time.sleep(self.health_check_interval)

    def get_next_server(self):
        with self.lock:
            if not self.available_servers:
                raise Exception("No available servers")
            server = self.available_servers[self.server_index]
            self.server_index = (self.server_index + 1) % len(self.available_servers)
            return server

    def handle_request(self, client_socket):
        try:
            request = client_socket.recv(1024).decode()
            server = self.get_next_server()
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_host, server_port = server.split(":")
            server_socket.connect((server_host, int(server_port)))
            server_socket.sendall(request.encode())
            response = server_socket.recv(4096)
            client_socket.sendall(response)
            server_socket.close()
        except Exception as e:
            client_socket.sendall(f"HTTP/1.1 500 Internal Server Error\n\n{str(e)}".encode())
        finally:
            client_socket.close()

    def start(self, host="0.0.0.0", port=80):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Load Balancer started on {host}:{port}")
        while True:
            client_socket, _ = server_socket.accept()
            threading.Thread(target=self.handle_request, args=(client_socket,), daemon=True).start()

if __name__ == "__main__":
    servers = ["localhost:8080", "localhost:8081", "localhost:8082"]
    load_balancer = LoadBalancer(servers, health_check_url="/", health_check_interval=10)
    load_balancer.start(host="localhost", port=80)
