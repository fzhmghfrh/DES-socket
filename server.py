import des_ecb as des
import socket

def start_server():
    server_address = 'localhost'
    server_port = 3000
    encryption_key = 'D4AF3BA2C945ED58'

    socket_server = socket.socket()
    socket_server.bind((server_address, server_port))

    print(f"Server is running at {server_address}:{server_port}")

    socket_server.listen(2)
    connection, client_address = socket_server.accept()
    print(f"Accepted connection from: {client_address}")

    while True:
        received_data = connection.recv(1024).decode()
        if not received_data:
            print("No data received. Closing connection.")
            break
        
        print(f"Data received from client: {received_data}")

        decrypted_message = des.des_decrypt(received_data, encryption_key)
        print(f"Decrypted message: {decrypted_message}\n")

        reply_message = input('Text to send back to client: ')
        encrypted_reply = des.des_encrypt(reply_message, encryption_key)
        print(f"Sending encrypted message: {encrypted_reply}")

        connection.send(encrypted_reply.encode())

    connection.close()

if __name__ == '__main__':
    start_server()
