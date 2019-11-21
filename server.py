#! /usr/bin/python3.7
import socket
from threading import Thread


def write(sc, address, copies):
    filename = sc.recv(1024).decode('ascii')
    print('Recieved file name -', filename)
    if copies.get(filename) is None:
        copies[filename] = 1
    else:
        copies[filename] += 1
    print('Start writing the file -', filename)
    f = open('(Copy - ' + str(copies[filename]) + ') ' + filename, 'wb')
    read_from_buff = sc.recv(1024)
    f.write(read_from_buff)
    while read_from_buff:
        f.write(read_from_buff)
        read_from_buff = sc.recv(1024)
    f.close()
    sc.close()


def main():
    s = socket.socket()
    s.bind(("", 10000))
    s.listen(10)
    copies = dict()

    while True:
        sc, address = s.accept()
        print('New connection', address)
        # write(sc, address, copies)
        thread = Thread(target=write, args=(sc, address, copies))
        thread.start()
    s.close()


if __name__ == "__main__":
    main()
