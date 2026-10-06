import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(1)

print("[SERVER] Listening on", HOST, PORT)
print("[SERVER] Waiting for client...")

conn, addr = server.accept()

print("[SERVER] Client connected:", addr)

with conn:
    while True:
        command = input("RAT> ").strip()

        if command.lower() == "exit":
            conn.sendall(b"exit")
            print("[SERVER] Closing connection.")
            break

        if command not in ("whoami", "hostname", "sysinfo"):
            print("[SERVER] Allowed commands: whoami, hostname, sysinfo, exit")
            continue

        conn.sendall(command.encode())

        response = conn.recv(4096).decode(errors="replace")
        print("[CLIENT RESPONSE]")
        print(response)

server.close()