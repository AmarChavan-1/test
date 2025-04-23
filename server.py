import socket
import os

host = '127.0.0.1'
port = 5001

# Folder to save received files
folder_name = 'received_files'
os.makedirs(folder_name, exist_ok=True)

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
print("Server is waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

filename = conn.recv(1024).decode()
file_path = os.path.join(folder_name, filename)

with open(file_path, 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print(f"File '{filename}' received and saved in '{folder_name}/'.")
conn.close()
