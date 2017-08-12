import ipaddress
import os
#print(ipaddress.ip_address(234.455.566.66))
#print(ipaddress.ip_network('192.12.0.0/24'))
ipnet=ipaddress.ip_network(u'192.12.0.0/24')
for i in ipnet.hosts():
   # if
   #print(str(i))
   response=os.system('ping -c 1 -i 0.2 ' + str(i) + '&>/dev/null' )
   #print(response)
   if response == 0:
       print( i, " alive")
   else:
       print( i, " down")
