import des_ecb as des
import socket

def start_client():
    server_address = 'localhost'
    server_port = 3000
    encryption_key = 'D4AF3BA2C945ED58'

    socket_client = socket.socket()
    socket_client.connect((server_address, server_port))

    initial_message = input("Enter plain text: ")
    encrypted_initial = des.des_encrypt(initial_message, encryption_key)
    print(f"Initial encrypted text: {encrypted_initial}")

    while initial_message.lower().strip() != 'end':
        socket_client.send(encrypted_initial.encode())
        response_data = socket_client.recv(1024).decode()
        print(f"Server: {response_data}")

        decrypted_response = des.des_decrypt(response_data, encryption_key)
        print(f"Decrypted text from server: {decrypted_response}\n")

        initial_message = input("Enter new plain text: ")
        encrypted_initial = des.des_encrypt(initial_message, encryption_key)
        print(f"New encrypted text: {encrypted_initial}")

    socket_client.close()

if __name__ == '__main__':
    start_client()
