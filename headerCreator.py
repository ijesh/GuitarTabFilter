#!/usr/bin/python

import re
import sys
from sets import Set

if(len(sys.argv) < 2):
    print '''Usage: ./headerCreator [input file]'''
    sys.exit()

def addChords(headers, chords):
    for i in range(len(chords)-1):
       print chords
       print i
       #print headers[i]
       headers[i].add(chords[i])



debug=True
inputFile = sys.argv[1]
hdlr = open(inputFile)

headers = [Set() for i in xrange(8)]
print headers
for line in hdlr:
    #chords=line.split(",")
    chords = re.findall(r"[\w+]",line)
    addChords(headers, chords)

print headers

