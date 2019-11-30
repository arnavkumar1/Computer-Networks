from struct import unpack
import socket
import threading
from urllib.request import urlopen

hostnames = ['ec2-18-222-189-83.us-east-2.compute.amazonaws.com',
    	     'ec2-18-216-216-71.us-east-2.compute.amazonaws.com',
             'ec2-18-220-185-191.us-east-2.compute.amazonaws.com']

MEASUREMENT_PORT = 45564



def select_replica(client_ip):
    dic = {}
    for i in range(len(hostnames)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(hostnames[i])
        try:
            sock.connect((ip, MEASUREMENT_PORT))
            sock.sendall(tar)
            latency = sock.recv(1024)
        except socket.error as e:
            latency = 'inf'
        finally:
            sock.close()
        dic.update({ip: float(latency)})
    result =  dic
    sorted_result = sorted(result.items(), key=lambda e: e[1])
    return sorted_result[0][0]