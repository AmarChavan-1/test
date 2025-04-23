import socket
import os
host = '127.0.0.1'
port = 5001
filename = input("Enter the filename to send (e.g., test.txt): ")
if not os.path.exists(filename):
    print("File not found.")
    exit()
client_socket = socket.socket()
client_socket.connect((host, port))
print("Connected to Server!")
client_socket.send(filename.encode())
with open(filename, 'rb') as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.send(data)
print(f"File '{filename}' sent successfully.")
client_socket.close()
