#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import errno
import getopt
import os
import socket
import sys
from urllib.request import urlopen


def download(path, response, name):
		f = open(name, 'w')
		t = response.read()
		f.write(t.decode('utf-8'))
		f.close()


def parse(argvs):
    (port, origin) = (0, '')
    opts, args = getopt.getopt(argvs[1:], 'p:o:')
    for o, a in opts:
        if o == '-p':
            port = int(a)
        elif o == '-o':
            origin = a
        else:
            sys.exit('Usage: %s -p <port> -o <origin>' % argvs[0])
    return port, origin

if __name__ == '__main__':
    port_number, origin_server = parse(sys.argv)
    req = "https://www.geeksforgeeks.org/socket-programming-python/"
    file_name = ''
    num = 0
    for i in req:
    	num += ord(i)
    filename = str(num) + ".xml"
    path = "~/Desktop"
    res = urlopen(req)
    download(path, res, filename)
    