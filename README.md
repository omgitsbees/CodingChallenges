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

Redis-like Server in Python

This project implements a basic Redis-like server in Python. It supports a simple in-memory key-value store and basic Redis-like commands using the RESP (REdis Serialization Protocol) format for communication.
Features

    In-Memory Key-Value Store: Store and retrieve key-value pairs.
    RESP Serialization: Supports serialization and deserialization of commands and responses using RESP.
    Basic Commands:
        PING: Responds with PONG.
        ECHO <message>: Returns the message provided.
        SET <key> <value>: Stores a key-value pair.
        GET <key>: Retrieves the value for the specified key or nil if the key doesn't exist.
    Concurrent Clients: Supports multiple clients by handling each client connection in a separate thread.

Supported Commands

    PING:
        Description: Tests server connectivity.
        Example:

        makefile

    PING
    Response: PONG

ECHO <message>:

    Description: Returns the message sent.
    Example:

    vbnet

    ECHO "Hello, World"
    Response: "Hello, World"

SET <key> <value>:

    Description: Stores a key-value pair in memory.
    Example:

    vbnet

    SET name "John"
    Response: OK

GET <key>:

    Description: Retrieves the value for a given key.
    Example:

    vbnet

GET name
Response: "John"

If the key does not exist:

vbnet

        GET age
        Response: nil

How It Works

    Server Initialization: The server listens on the default Redis port 6379 (or any port of your choice) and accepts incoming connections.
    Handling Client Requests: Each client connection is handled on a separate thread to allow multiple clients to connect simultaneously.
    RESP Protocol: The server uses RESP to serialize and deserialize client commands and server responses.
    Command Processing: Basic commands like PING, ECHO, SET, and GET are processed by the server and appropriate responses are sent back to the client.

Installation
Prerequisites

    Python 3.x

Running the Server

    Clone the Repository:

    bash

git clone https://github.com/yourusername/redis-like-server.git
cd redis-like-server

Run the server:

bash

    python redis_server.py

    By default, the server will run on 127.0.0.1:6379. You can modify the host and port in the start_redis_server function.

Example Usage

You can interact with the server using telnet or any Redis client:

    Using Telnet:

    Open a terminal and run:

    bash

telnet 127.0.0.1 6379

Then you can enter commands like:

sql

PING
ECHO "Hello"
SET key1 "value1"
GET key1

Using a Python Redis Client:

You can also use the Python redis-py client:

python

    import redis

    r = redis.Redis(host='127.0.0.1', port=6379)

    r.ping()  # Should return True
    r.set('foo', 'bar')  # Set a key-value pair
    r.get('foo')  # Retrieve the value, should return b'bar'

Code Overview

    Serialization & Deserialization: The serialize and deserialize functions handle RESP protocol for communication.
    Command Handling: The handle_command function processes basic Redis commands (PING, ECHO, SET, GET).
    Threaded Client Handling: The client_handler function manages individual client connections in separate threads.
    Main Server: The start_redis_server function initializes the server, listens for client connections, and creates threads to handle them.

-------------------------------------------------------------------------------------------------------------------------------

Python uniq Command Implementation

This Python script mimics the behavior of the Unix uniq command, providing several functionalities such as displaying unique lines, counting occurrences, showing repeated lines, and showing unique lines only. It can process input from either standard input or a file, and output results to standard output or a file.
Features

    Default Behavior: Display unique lines while removing consecutive duplicates.
    Count Occurrences (-c): Display each line along with the number of occurrences.
    Repeated Lines (-d): Show only lines that are repeated.
    Unique Lines (-u): Show only lines that appear exactly once.

Usage

The script can be run from the command line with different options and file inputs:

css

python uniq.py [OPTION]... [INPUT] [OUTPUT]

Options

    -c: Prefix each line with the number of occurrences.
    -d: Only display repeated lines.
    -u: Only display unique lines.

Input

    INPUT: The file to be processed. If not provided or if - is used, the script will read from standard input.

Output

    OUTPUT: The file to write the results to. If not provided, the output will be printed to standard output.

Examples
Default Behavior

To display unique lines while removing consecutive duplicates:

bash

python uniq.py input.txt

Count Occurrences

To count how many times each line appears in a file:

bash

python uniq.py -c input.txt

Display Repeated Lines

To display only repeated lines:

bash

python uniq.py -d input.txt

Display Unique Lines

To display only lines that appear exactly once:

bash

python uniq.py -u input.txt

Output to a File

You can also specify an output file:

bash

python uniq.py -c input.txt output.txt

This will write the result to output.txt.
Error Handling

    If the input file does not exist, an error message will be displayed: File <input file> not found.
    If no input file is provided, the script will read from stdin.

Installation

No special installation is required. The script only needs Python 3.x.
Prerequisites

    Python 3.x installed on your system.

Running the Tests

You can test the script by passing files or input through stdin. For example:

bash

cat sample.txt | python uniq.py -c

-------------------------------------------------------------------------------------------------------------------------------

