import socket


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(("8.8.8.8", 80))
    HOST = s.getsockname()[0]

PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    s.listen()
    print(f"Servidor ouvindo em {HOST}:{PORT}")

    conn, addr = s.accept()

    with conn:
        print(f'Conectado por {addr}')
        while True:
            command = input('Command: ')
            conn.sendall(command.encode())

            if command == 'exit':
                print("Bye!")
                conn.close()
                break

            data = conn.recv(4096)
            print(f'{addr}: {data.decode()}')
