import socket
sock = socket.socket()
sock.connect(('127.0.0.1',9090))

def exec(command):
    if not command:
        exec(command)
    elif command == "exit":
        quit()
    else:
        sock.send(command.encode())
while True:
    command = input("Type Command: ")
    exec(command)
    data = sock.recv(1024).decode()
    print("last command: " + data)

