import argparse 

desc='for printing arguments'

parser=argparse.ArgumentParser(description=desc)
parser.add_argument('host',type=str,help='hostname for scanning port')
parser.add_argument('port',type=int, help='port to be scanned for the host')
args=parser.parse_args()

host=args.host
port=args.port

print host,port




