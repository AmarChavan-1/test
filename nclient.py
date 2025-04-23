import socket
import os

host = '127.0.0.1'
port = 5001

# Create a socket to connect to the server
client_socket = socket.socket()
client_socket.connect((host, port))
print("Connected to Server!")

def send_file():
    filename = input("Enter the filename to send (e.g., test.txt): ")
    if not os.path.exists(filename):
        print("File not found.")
        return
    client_socket.send(filename.encode())  # Send the filename to the server
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)  # Send the file data
    print(f"File '{filename}' sent successfully.")

def receive_file():
    filename_to_receive = input("Enter the filename to receive from the server (e.g., received.txt): ")
    client_socket.send(filename_to_receive.encode())  # Request file from the server
    with open(filename_to_receive, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)  # Write received data to the file
    print(f"File '{filename_to_receive}' received successfully.")

# Main loop for client interaction
while True:
    print("\nClient Menu:")
    print("1. Send file to server")
    print("2. Receive file from server")
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

client_socket.close()
