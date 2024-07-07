from vidstream import ScreenShareClient
import threading


c = ScreenShareClient(host='192.168.0.116', port=33333)

t = threading.Thread(target=c.start_stream)
t.start()

while input('') != 'exit':
    continue

c.stop_stream()
