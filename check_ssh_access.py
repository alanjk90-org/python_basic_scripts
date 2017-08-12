import argparse
import socket 

parser = argparse.ArgumentParser(description = 'for checking ssh login status')
#parser.add_argument(host, nargs = 1)
parser.add_argument('host', help='Host name you want to scan')
args = parser.parse_args()

ip = args.host
#ip = socket.gethostbyname(host)
#print ip

#creating socket 
sock = socket.socket()
sock.settimeout(0.5)
r = sock.connect_ex((ip,22))
if r == 0: print "ssh port is accessible"
else: print "ssh port is not open"






