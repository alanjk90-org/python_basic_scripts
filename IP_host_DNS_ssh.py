import socket
import dns.resolver
import argparse
import os
import pyping

parser=argparse.ArgumentParser()
parser.add_argument('host', type = str)
parser.add_argument('record', type = str, nargs = '?' )
args=parser.parse_args()

host=args.host
record=args.record
print '=' * 10

#print host,record


#get ip from hostname
ip=socket.gethostbyname(host)
print "ip is ", ip
print '=' * 10

#print domain name from ip
domain_name = socket.gethostbyaddr(ip)
print "domain name is ", domain_name 
fqdn = socket.getfqdn(ip)
print "FQDN is ", fqdn
print '=' * 10

#get dns records of a domain
myResolver = dns.resolver.Resolver()
myAnswers = myResolver.query(host, record)
for rdata in myAnswers:
    print "%s record for %s host is %s" %(record, host, rdata)
print '=' * 10

#ping a host or ip
#os.system("ping -c 1 " + host)
response = pyping.ping(host)
if response.ret_code == 0: print "host is up"
else: print "host is not up"
print '=' * 10

