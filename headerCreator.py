#!/usr/bin/python

import re
import sys
from sets import Set

if(len(sys.argv) < 3):
    print '''Usage: ./headerCreator [input file] [output file]'''
    sys.exit()

def addChords(headers, chords):
    for i in range(len(chords)):
       #print chords
       #print i
       #print headers[i]
       headers[i].add(chords[i])



debug=True
inputFile = sys.argv[1]
outputFile = sys.argv[2]
hdlr = open(inputFile)

headers = [Set() for i in xrange(8)]
#print headers
for line in hdlr:
    #chords=line.split(",")
    #print line
    chords = re.findall(r"(\w+#*\w*)",line)
    addChords(headers, chords)

hdlr2 = open(outputFile, "w")
for column in headers:
  hdlr2.write(",".join(column))
  hdlr2.write('\n')
print headers

