import socket, urlparse, select


HOST = 'led-pc.office.remote.net'
PORT = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pollerObject = select.poll()

pollerObject.register(sock, select.POLLIN)


if __name__ == '__main__':
    sock.bind((HOST,PORT))
    sock.listen(5)
    print('serving HTTP on port', PORT)
    while True:
        serverLoop()
