#! /usr/bin/python3.7
import socket

if __name__ == '__main__':
    s = socket.socket()
    print('Write your source IP address')
    ip = input()
    print('Write your source Port number')
    port = int(input())
    s.connect((ip, port))
    print('Write your file name')
    filename = input().encode('ascii')
    s.send(filename)
    print('Sent file name')
    f = open(filename, "rb")
    f_size = len(f.read())
    left_size = f_size
    f = open(filename, "rb")
    current_buff = f.read(1024)
    left_size = left_size - len(current_buff)
    print(((f_size - left_size) / f_size) * 100, '%')
    while current_buff:
        s.send(current_buff)
        current_buff = f.read(1024)
        left_size = left_size - len(current_buff)
        print(((f_size - left_size) / f_size) * 100, '%')
    print('Sending file finished')
    s.close()
