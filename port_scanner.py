import socket, argparse
#from sys import argv

parser=argparse.ArgumentParser()
parser.add_argument('host',type=str)
parser.add_argument('port',type=int)
args=parser.parse_args()


#script,host,port=argv  
#port=int(port)

host=args.host
port=args.port

print "host is %s and port is %d "%(host,port)

sock=socket.socket()
sock.settimeout(0.5)
r=sock.connect_ex((host,port))
if r == 0:
    print port,"is up"
else:
    print "unable to connect"

sock.close()
