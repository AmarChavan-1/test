import socket
import os

host = '127.0.0.1'
port = 5001

# Folder to save received files
folder_name = 'received_files'
os.makedirs(folder_name, exist_ok=True)

# Create a socket for the server
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
print("Server is waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

def send_file():
    filename_to_send = input("Enter the filename to send to the client (e.g., send_back.txt): ")
    if not os.path.exists(filename_to_send):
        print("File not found.")
        return
    conn.send(filename_to_send.encode())  # Send the filename to the client
    with open(filename_to_send, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            conn.send(data)  # Send the file data
    print(f"File '{filename_to_send}' sent successfully.")

def receive_file():
    filename = conn.recv(1024).decode()  # Receive the filename from the client
    file_path = os.path.join(folder_name, filename)

    with open(file_path, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)  # Write received data to the file
    print(f"File '{filename}' received and saved in '{folder_name}/'.")

# Main loop for server interaction
while True:
    print("\nServer Menu:")
    print("1. Send file to client")
    print("2. Receive file from client")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        send_file()
    elif choice == '2':
        receive_file()
    elif choice == '3':
        print("Closing connection.")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

conn.close()
