#!/usr/bin/env python3

from socket import *
import sys

def recvall(sock, length):
    data = b''
    while len(data) < length:
        nextbytes = sock.recv(length - len(data))
        if not nextbytes:
            raise EOFError('was supposed to receive %d bytes'
                ' but only received %d bytes' % (length, len(data)))
        data += nextbytes
    return data

def server(interface, port):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSock.bind((interface, port))
    serverSock.listen(1)
    print('Listening at', serverSock.getsockname())
    while True:
        connSock, sockname = serverSock.accept()
        print('Accepted a connection from', sockname)

        f = connSock.makefile(mode='r')

        for line in f:
            print('Received line:', line, end='')

        f.close()
        connSock.close()
        print('Connection closed')

def client(host, port):
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((host, port))
    
    print('Connected from', clientSock.getsockname())

    lines = "Hello server!\nThis is line two.\nGoodbye!\n"
    clientSock.sendall(lines.encode('utf-8'))

    clientSock.close()

if __name__ == '__main__':
    roles = {'client': client, 'server': server}
    function = roles[sys.argv[1]]
    host = sys.argv[2]
    port = int(sys.argv[3])
    function(host, port)