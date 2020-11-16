from pythonping import ping
import threading

def _ping(name):
    ping(name, verbose=True)

hosts = ['8.8.8.8', '93.175.2.172', '17.253.144.10', '93.175.29.204']
for i in hosts:
    threading.Thread(target=_ping, args = (i,)).start()
