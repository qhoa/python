import socket
import time
from datetime import datetime

host = input("IP Address: ")
port = input("Port: ")
count = input("Count: ")
server = ((host), int(port))
print(server)
n = int(count)
while n > 0:
    n -= 1
    time.sleep(2)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(server)
    if result == 0:
        print(n,".","Port is open", server, "at", datetime.now().time())
    else:
        print(n,".","Port is close", server, "at", datetime.now().time())
    sock.close()
else:
    print("End !!!!!")