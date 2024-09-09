Basic Web Server

This project demonstrates the implementation of a basic HTTP web server in Python. The server listens for incoming client requests, processes them, and returns either static HTML files or a simple message based on the request. It supports basic HTTP/1.1 GET requests and serves documents from a specified directory.
Features

    Basic HTTP/1.1 Support: Handles basic GET requests and returns static HTML files.
    Custom Document Root: You can configure the server to serve files only from a specified directory (default: www folder).
    404 Error Handling: Responds with a "404 Not Found" error for invalid paths.
    Concurrent Clients: Supports multiple client connections by using threading to handle each connection in parallel.
    Security Measures: Restricts file access to a specific directory to avoid unauthorized file access.

How It Works

    Step 1 - Basic HTTP Server: The server listens on port 80 (default HTTP port) and accepts incoming connections.
    Step 2 - Serving HTML Files: Based on the client's request path, the server returns either the requested file (e.g., index.html) or an error message if the file is not found.
    Step 3 - Concurrent Clients: The server uses threads to handle multiple client requests concurrently without blocking other connections.
    Step 4 - Document Root Security: The server restricts access to files within the www folder to prevent unauthorized access to sensitive files outside the directory.

Setup Instructions
Prerequisites

    Python 3.x installed on your machine
    Basic understanding of networking and HTTP

Installation

    Clone this repository:

    bash

git clone https://github.com/yourusername/basic-web-server.git
cd basic-web-server

Create a www directory:

bash

mkdir www

Add an index.html file (or any other HTML files you want to serve):

html

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

Running the Server

    Start the server:

    bash

python web_server.py

This will start the web server and listen on 127.0.0.1:80 by default.

Make a request:

You can test the server using a web browser or a tool like curl:

bash

    curl http://127.0.0.1/

    If you have an index.html file in the www directory, it will be returned by the server.

Customizing the Server

    Port Configuration: You can modify the server to listen on a different port by updating the server_port in the code.
    Document Root: Change the www folder path in the code to customize where the server serves files from.

Example Usage

    Accessing HTML Files: If index.html exists in the www directory, visiting http://127.0.0.1/ will return the HTML page.

    bash

curl http://127.0.0.1/

Response:

http

HTTP/1.1 200 OK

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

Handling 404 Errors: If a requested file is not found, the server will return a 404 Not Found error:

bash

curl http://127.0.0.1/invalid.html

Response:

http

HTTP/1.1 404 Not Found

-------------------------------------------------------------------------------------------------------------------------------

