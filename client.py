import socket
import platform
import getpass

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("[CLIENT] Connected to server.")

try:
    while True:
        command = client.recv(1024).decode()

        if not command or command == "exit":
            break

        if command == "whoami":
            result = getpass.getuser()

        elif command == "hostname":
            result = platform.node()

        elif command == "sysinfo":
            result = (
                f"OS: {platform.system()}\n"
                f"Version: {platform.version()}\n"
                f"Architecture: {platform.machine()}\n"
                f"Python: {platform.python_version()}"
            )

        else:
            result = "Command not permitted."

        client.sendall(result.encode())

finally:
    client.close()
    print("[CLIENT] Connection closed.")