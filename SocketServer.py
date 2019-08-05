import socket
import os
sock = socket.socket()
sock.bind(('127.0.0.1',9090))
print("Сервер запущен! \n")
sock.listen(1)
conn, addr = sock.accept()

while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    os.system(data)
    conn.send(data.encode().upper())

conn.close()