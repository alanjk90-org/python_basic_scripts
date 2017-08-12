import ipaddress
import os

network=ipaddress.ip_network(u'192.168.1.0/24')

for ip in network:
    response=os.system('ping -c1 ' + str(ip) + '>/dev/null' )
    if response == 0:
        print ip, "alive" 
    else:
        print ip, "down"
       