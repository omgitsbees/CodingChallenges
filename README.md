# Python Diff Tool

This is a Python implementation of a `diff` tool that compares the differences between two files, based on the Myers algorithm (used by Git). The tool can find the **longest common subsequence (LCS)** between two strings, handle arrays of strings (i.e., lines from a file), and ultimately display the differences between two files in a format similar to the Unix `diff` command.

## Features

- **Longest Common Subsequence (LCS)**: Finds the common subsequence between two strings.
- **Array of Strings Comparison**: Applies the LCS algorithm to arrays of strings (file lines).
- **Diff Output**: Generates the differences between two files or arrays of strings, marking lines that are added, removed, or unchanged.
- **Command Line Interface**: Compares two text files and prints the differences to the terminal.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Testing](#testing)
4. [Examples](#examples)
5. [Future Improvements](#future-improvements)

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/python-diff-tool.git
    cd python-diff-tool
    ```

2. Install Python (if not already installed):
    - Ensure you have Python 3.5 or later installed on your machine.
    - You can download it from [python.org](https://www.python.org/).

3. Install any required packages (if needed):
    ```bash
    pip install -r requirements.txt
    ```
   *(Note: The tool doesn't require any external libraries by default.)*

## Usage

The Diff Tool can be run from the command line to compare two files. To execute it:

```bash
python diff_tool.py file1.txt file2.txt

Output Format

The tool will print out the differences between the files:

    Lines removed from the first file are prefixed with <.
    Lines added to the second file are prefixed with >.
    Lines that remain unchanged are prefixed with a space.

Command-Line Arguments

    file1.txt: The original file.
    file2.txt: The new file you want to compare with the original.

Testing

Unit tests are included to ensure the correctness of the LCS algorithm and the diff tool. To run the tests, use the following command:

bash

python -m unittest diff_tool.py

Examples
Example 1

Comparing two simple files:

file1.txt

kotlin

This is a test which contains:
this is the lcs

file2.txt

kotlin

this is the lcs
we're testing

Command:

bash

python diff_tool.py file1.txt file2.txt

Output:

kotlin

< This is a test which contains:
  this is the lcs
> we're testing

Example 2

Comparing two arrays of strings:

Input Arrays:

python

lines1 = ["A", "B", "C"]
lines2 = ["A", "C", "D"]

Output:

css

  A
< B
  C
> D

-------------------------------------------------------------------------------------------------------------------------------

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

Python Grep Tool

A Python implementation of the Unix grep tool. This tool allows you to search files and directories for specific patterns, with options for case-insensitive search, inverted matches, and recursive directory traversal.
Features

    Basic Grep Functionality: Search for a specific pattern in one or more files.
    Case Insensitive Search: Use the -i option to perform case-insensitive searches.
    Inverted Match: Use the -v option to print lines that do not match the pattern.
    Recursive Search: Use the -r option to search directories recursively.
    Supports \d and \w in Patterns: Patterns like \d (digits) and \w (word characters) are supported.

Usage

bash

python grep.py [OPTIONS] PATTERN FILES...

Arguments

    PATTERN: The regex pattern to search for in the files.
    FILES: One or more files or directories to search in.

Options

    -r, --recursive: Recursively search directories.
    -v, --invert: Invert the match, i.e., show lines that do not match the pattern.
    -i, --ignore-case: Perform case-insensitive search.

Examples
Basic Search

bash

python grep.py 'search_term' file.txt

This will search for the term 'search_term' in file.txt.
Case-Insensitive Search

bash

python grep.py -i 'search_term' file.txt

This will search for the term 'search_term' in file.txt ignoring case.
Inverted Match

bash

python grep.py -v 'search_term' file.txt

This will print all lines in file.txt that do not match 'search_term'.
Recursive Search in a Directory

bash

python grep.py -r 'search_term' /path/to/directory

This will search for the term 'search_term' in all files within the specified directory and its subdirectories.
Combined Example

bash

python grep.py -rvi 'search_term' /path/to/directory

This will perform a recursive, case-insensitive search and show lines that do not match 'search_term'.
Installation

No installation required. Simply clone the repository and run the script using Python 3.x.

bash

git clone https://github.com/your-username/grep-python.git
cd grep-python
python grep.py [OPTIONS] PATTERN FILES...

-------------------------------------------------------------------------------------------------------------------------------

URL Shortener

A simple URL shortener built using Flask and SQLite. Users can shorten URLs via a web interface, and the app provides a shortened URL for easy sharing.
Features

    Shorten long URLs
    Redirect to the original URL when the shortened URL is accessed
    Web UI for submitting and displaying shortened URLs
    SQLite database to store URL mappings

Demo

(Replace this with an actual demo GIF/image if you have one)
Prerequisites

Before running the application, make sure you have the following installed:

    Python 3.x
    pip (Python package installer)

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/url-shortener.git
cd url-shortener

Create a virtual environment (optional but recommended):

bash

python3 -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate

Install the dependencies:

bash

pip install -r requirements.txt

Create the SQLite database:

bash

    flask shell
    from app import db
    db.create_all()
    exit()

Usage

    Run the Flask server:

    bash

    flask run

    Access the application:

    Open a browser and navigate to http://localhost:5000. You will see the UI for the URL shortener where you can input URLs and get a shortened link.

Project Structure

graphql

url-shortener/
│
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # HTML template for the web UI
├── static/
│   └── style.css         # Optional CSS for custom styling
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── urls.db               # SQLite database (auto-generated)

How It Works

    The user submits a URL via the web form.
    The server generates a unique 8-character short code for the URL.
    The original URL and short code are stored in the SQLite database.
    The user receives a shortened URL that points to the app.
    When the shortened URL is accessed, the app looks up the corresponding original URL and redirects the user.

API Endpoints
1. /shorten (POST)

Shorten a given URL.

    Request body: url (the long URL)
    Response: The shortened URL.

2. /<short_code> (GET)

Redirects to the original URL based on the short code.

    Response: Redirect to the original long URL.

Example

    Input: https://www.example.com/some/long/url
    Output: http://localhost:5000/abc12345
    Visiting http://localhost:5000/abc12345 redirects to the original URL.

-------------------------------------------------------------------------------------------------------------------------------

Custom Command Line Shell (ccsh)

This project implements a custom command line shell named ccsh (Coding Challenges Shell), built in Python. The shell provides basic functionality such as executing system commands, handling pipes, managing command history, and responding to built-in commands like cd, pwd, exit, and history.

Table of Contents

	•	Overview
	•	Features
	•	Installation
	•	Usage
	•	Built-in Commands
	•	Example
	•	Command History
	•	Signal Handling
	•	Contributing
	•	License

Overview

The ccsh shell allows users to interact with the underlying operating system by running commands, chaining them with pipes, and managing directories. It mimics the functionality of a typical Unix shell with some custom features. This project is designed as a coding challenge to build a working shell from scratch, implementing features such as command execution, piping, and command history management.

Features

	•	Execute System Commands: Run basic commands like ls, cat, pwd, etc.
	•	Pipes Support: Chain commands using pipes (|) to pass output from one command to the next.
	•	Built-in Commands: Implement commands like cd (change directory), pwd (print working directory), exit (terminate shell), and history (show command history).
	•	Command History: Supports scrolling through previous commands using up/down arrow keys and saving history to disk.
	•	Signal Handling: Captures signals such as SIGINT (Ctrl-C) to prevent shell termination.

Installation

	1.	Clone the repository:

git clone https://github.com/your-username/ccsh.git
cd ccsh

	2.	Install required packages:
No external packages are required, as this shell only relies on Python’s standard library.
	3.	Run the shell:
python ccsh.py

Usage

Once the shell is running, you can enter any command as you would in a normal shell. Commands are executed in the underlying operating system environment.

uilt-in Commands

	•	cd: Change the current directory.
	•	Example: ccsh> cd /path/to/directory
	•	pwd: Print the current working directory.
	•	Example: ccsh> pwd
	•	exit: Exit the shell.
	•	history: Display the list of previously executed commands.

Command History

	•	The shell automatically saves command history to the user’s home directory in a file named .ccsh_history.
	•	The command history is loaded when the shell starts, and previous commands can be accessed using the up/down arrow keys.
	•	Use the history command to display the list of all commands executed in the current session.

Signal Handling

	•	Ctrl-C (SIGINT): When pressed, the signal will terminate the running command without exiting the shell itself.
	•	This allows users to interrupt long-running commands but remain in the shell environment.

-------------------------------------------------------------------------------
