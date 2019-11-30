import random
import getopt
import socket
import struct
import sys

from findnearestserver import select_replica

RECORD = {'ec2-18-222-189-83.us-east-2.compute.amazonaws.com': '18.222.189.83',
          'ec2-18-216-216-71.us-east-2.compute.amazonaws.com': '18.216.216.71',
          'ec2-18-220-185-191.us-east-2.compute.amazonaws.com': '18.220.185.191'}



def parse(argvs):
    port = 0
    name = ''
    opts, args = getopt.getopt(argvs[1:], 'p:n:')
    for o, a in opts:
        if o == '-p':
            port = int(a)
        elif o == '-n':
            name = a
        else:
            sys.exit('Usage: %s -p <port> -o <origin>' % argvs[0])
    return port, name


if __name__ == '__main__':
	(port_number, cdn_name) = parse(sys.argv)
	client_ip = '192.168.116.91'
	ip = select_replica(client_ip)
	print (ip)

