import os 
import sys 
import subprocess 
import signal 
import readline 

# History file location
HISTORY_FILE = os.path.expanduser("~/.ccsh_history")

def load_history():
    """Load command history from file."""
    if os.path.exists(HISTORY_FILE):
        readline.read_history_file(HISTORY_FILE)
        
def save_history():
    """Save command history to file."""
    readline.write_history_file(HISTORY_FILE)
    
def sigint_handler(signum, frame):
    """"Handle SIGINT (Ctrl-C) to prevent shell from terminating."""
    print("\nccsh> ", end='', flush=True)

def change_directory(path):
    """Builtin 'cd' command to change directories."""
    try:
        os.chdir(path)
    except FileNotFoundError as e:
        print(f"cd: {e}")
        
def get_current_directory():
    """Builtin 'pwd' command to print current working directory."""
    print(os.getcwd())
    
def execute_command(command_parts):
    """Execute a system command, handling pipes if necessary."""
    if "|" in command_parts:
        # handle piping
        processes = []
        previous_pipe = None 
        
        for i, part in enumerate(command_parts.split("|")):
            command = part.strip().split()
            if i == 0:
                # First command
                previous_pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
            else:
                # Intermediate commands
                current_pipe = subprocess.Popen(command, stdin=previous_pipe.stdout, stdout=subprocess.PIPE)
                previous_pipe.stdout.close()
                previous_pipe = current_pipe 
    else:
        # Handle single command
        try:
            subprocess.run(command_parts.split())
        except FileNotFoundError:
            print("No such file or directory (os error 2)")
            
def main():
    # Load history from file
    load_history()
    
    # Handle SIGINT (Ctrl-C)
    signal.signal(signal.SIGINT, sigint_handler)
    
    while True:
        try:
            # Display custom shell prompt
            command_input = input("ccsh> ").strip()
            
            # Handle 'exit' command
            if command_input =="exit":
                save_history()
                sys.exit(0)
                
            # Handle 'exit' command
            if command_input == "exist":
                save_history()
                sys.exit(0)
                
            # Handle 'cd' command
            elif command_input.startswith("cd "):
                change_directory(command_input.split(" ", 1)[1])
            
            # Handle 'pwd' command
            elif command_input == "pwd":
                get_current_directory()
                
            # Handle 'history' command
            elif command_input == "history":
                for i in range(readline.get_current_history_length()):
                    print(readline.get_history_item(i + 1))
            
            # Handle external commands
            else:
                execute_command(command_input)
        
        except EOFError:
            # Gracefully exit on Ctrl-D
            save_history()
            print("\nExiting ccsh")
            sys.exit(0)
            
if __name__ == "__main__":
    main()