import argparse
import os

parser= argparse.ArgumentParser(description="script for executing bash commands from command line")
parser.add_argument("command", type=str, nargs="+", help="enter bash commands and if command contains \"-\" enter commands inside single quates")
args=parser.parse_args()

#print (str(args.command))
#print(args)
#print(args.command)
#print(type(args))
#print (str(args.command))
#print(type(str(args.command)))

commands=' '.join(args.command)

print(commands)

os.system('pwd')
os.system('{}'.format(commands))
