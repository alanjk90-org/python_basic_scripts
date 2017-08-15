#!/usr/bin/env python

import re
from StringIO import StringIO

def syndax():
    print "\n\n" + "="*30
    print "\033[1;33mSyndax for printing strings in color \033[1;m"
    print '-'*30
    print "\033[1;31m" + " " + "\\033[1;[30-48]mstring\\033[1;m" + "\033[1;m"
    print '-'*30
    print "\033[1;31m<< \\033[1; #startsyndax>>  << 30-48 #colorcode>> << m >> << string >> << \\033[1; #ending syndax>> << m >>\033[1;m"
    print '='*30

def stringfile():
    colrfile=r"""print '\033[1;30mGray like Ghost\033[1;m',
print '\033[1;31mRed like Radish\033[1;m'
print '\033[1;32mGreen like Grass\033[1;m'
print '\033[1;33mYellow like Yolk\033[1;m'
print '\033[1;34mBlue like Blood\033[1;m'
print '\033[1;35mMagenta like Mimosa\033[1;m'
print '\033[1;36mCyan like Caribbean\033[1;m'
print '\033[1;37mWhite like Whipped Cream\033[1;m'
print '\033[1;38mCrimson like Chianti\033[1;m'
print '\033[1;41mHighlighted Red like Radish\033[1;m'
print '\033[1;42mHighlighted Green like Grass\033[1;m'
print '\033[1;43mHighlighted Brown like Bear\033[1;m'
print '\033[1;44mHighlighted Blue like Blood\033[1;m'
print '\033[1;45mHighlighted Magenta like Mimosa\033[1;m'
print '\033[1;46mHighlighted Cyan like Caribbean\033[1;m'
print '\033[1;47mHighlighted Gray like Ghost\033[1;m'
print '\033[1;48mHighlighted Crimson like Chianti\033[1;m'
"""
    colrfile=StringIO(colrfile)
    return colrfile

def gettingcolor():
    print "\n\n" + "="*30 + "\n" + "color" + " " + "code" + "\n" + "-"*30
    for line in stringfile():
        if line.startswith("print '\\"):
            #print line
            match= re.match(re.compile(r"""print                                  #print
                                       \s'                                   #space and single quat
                                       (?P<startsyndax>\\[0-9]{3}\[\d;)      #starting syndax for coloring
                                       (?P<colorcode>[0-9]{2})               #color code
                                       m                                     #m
                                       (?P<color>[A-Za-z]+?)                 #color
                                       \s                                    #space
                                       (.*?)                                 #remaining string
                                       (?P<endsyndax>\1)                     #ending syndax for coloring
                                       """, re.VERBOSE), line)
            #print match.groups()
            print '\033[1;' + str(match.groupdict()['colorcode']) + 'm' + str(match.groupdict()['color']) + ' ' + str(match.groupdict()['colorcode']) + '\033[1;m'
    print "="*30 + "\n\n"

if __name__ == '__main__':
    syndax()
    #stringfile()
    #print stringfile().read()
    gettingcolor()
