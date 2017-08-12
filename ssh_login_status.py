#from pexpect import pxssh
#
#host = raw_input('hostname> ')
#myusername = raw_input('username> ')
#mypassword = raw_input('password> ')
#
#s = pxssh.pxssh()
#if not s.login( host, myusername, mypassword ):
#    print "ssh session fail to login"
#    print str(s)
#else:
#    print "ssh sessoin successfully logged in"
#    s.sendline('uptime')
#    s.promt()
#    print s.before
#    s.logout()

import argparse
import socket 
import sys 

parser=argparse.ArgumentParser(description='for checking ssh access')
#parser.add_argument('host',type=str,help='hostname for scanning port')
parser.add_argument('host', help = "hostname")
args=parser.parse_args()

host = args.host
#script, hostname = sys.argv

s = socket.socket()
try:
    s.connect((host, 22))
    print "port 22 is accessible"
except socket.error as e:
    print "Error on connect: %s" %e



