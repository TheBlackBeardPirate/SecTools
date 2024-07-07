from vidstream import StreamingServer
import threading


s = StreamingServer(host='192.168.0.116', port=33333)

t = threading.Thread(target=s.start_server)
t.start()

while input('') != 'exit':
    continue

s.stop_server()
