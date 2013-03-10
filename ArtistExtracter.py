import sys
from sets import Set

if(len(sys.argv) < 3):
	print "Usage: python ArtistExtracter.py inputFile outputFile [-o] [-i]"
	print "\t-o = output only artists"
	print "\t-i = input genre for artists"
	sys.exit()

############# Arguments ##############
debug = False
inputFile = sys.argv[1]
outputFile = sys.argv[2]
onlyArtist = False
inputGenre = False
if len(sys.argv) > 3:
	#print sys.argv
	if sys.argv[3]=='-o':
		onlyArtist = True
	else:
		print "Argument "+sys.argv[3]+" not recognized!"
		sys.exit()
	if len(sys.argv) > 4:
		if sys.argv[4]=='-i':
			inputGenre = True
		else:
			print "Argument "+sys.argv[3]+" not recognized!"
			sys.exit()

def extractSong(song):
	index = song.find('_ver')
	#print index
	if( index == -1):
		index = song.find('_crd')
		if(index == -1):
			index = 0
	return song[:index]

def getInput():
	print "Enter genre for "+ value +":",
	genre = raw_input()
	if not genre:
		return getInput()
	else:
		return genre

#print sys.argv[1]
hdl = open(inputFile)
song_artist_hash = {}
writer = open(outputFile, 'w')
for line in hdl:
	if(line.find('http') != -1):
		words = line.split('/')
		artist = words[-2]
		song = extractSong(words[-1])
		if song not in song_artist_hash:
			song_artist_hash[song] = artist

for key, value in song_artist_hash.iteritems():
	if(onlyArtist):
		if(inputGenre):
			genre = getInput()
		writer.write(value+" "+genre+ "\n")
	else:
		writer.write(key + "\t" + value+ "\n")

if(debug):
	songText = "everlasting_love_crd.htm"
	print extractSong(songText)