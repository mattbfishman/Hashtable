import re
import string
from datetime import datetime
import time
import sys
import hashlib

class fileInput():
	global values
	global size

   	global hash0, hashA, hashB, hashC, hashD, hashE, hashF
   	def hash0(word, size):
   		# A sanity check hash function
   		return 0 #values[word[0]] % size

   	def hashA(word, size):
		key = 0
		for letters in word:
			#print tempNumber #test code
			key = ord(letters) + key
		location = key % size
		return location

   	def hashB(word, size):
		key = 1
		for letters in word:
			#print tempNumber #test code
			key = (ord(letters) * key)
		location = key % size
                if location < 0: location = -location   # Make sure it is positive (overflow)!
		return location

   	def hashC(word, size):
		key = 0
		for letters in word:
			key = ((key*101) + ord(letters)) % size
		return key

	def hashD(word, size):
		key = 0
		m = True
		for letters in word:
			if m == True: 
				key = (key * (ord(letters)<<3)) % size
				m = False
			else:
				key = (key + (ord(letters))) % size
				m = True
		return key

	def hashE(word, size):
		key = 0
		for letters in word:
			key = (key + (ord(letters)<<6) + (ord(letters)<<16) - ord(letters)) % size
		return key

	def hashF(word, size):
		a = hashlib.md5(word)
		b = a.hexdigest()
		as_int = int(b,16)
		return as_int %size #bin(as_int)[2:] #converts to binary string 

	def runTest(tempArray, hashTable, h):
		count = 0
		for tempNumber in tempArray:
			#print tempNumber #test code
			location = h(tempNumber, size)
			while hashTable[location] != '0' and hashTable[location] != tempNumber:
				if  len(hashTable) <= location + 1:
				 	location = 0
				else:
				 	location = location + 1
			if hashTable[location] != tempNumber:
                                # It is a unique word - add it.
				hashTable[location] = tempNumber
                                count += 1    # Keep track of the number of unique words
		print count, 'unique words'

	tempArray = []

        # Get the file name from command line argument or use a default file name.
	if len(sys.argv) < 2:
		fileName = 'words.txt'
	else:
		fileName = sys.argv[1]

	print "Opening ", fileName, " for processing."
	f = open(fileName, 'r')

	for line in f:
		line =  line.upper()
		words = line.split()
		for word in words:
			word = re.sub(r'[^a-zA-Z 0-9]', '', word) #removes the special characters
			#print(word) 
			if re.match("[^0-9]", word):
				if any(ch.isdigit() for ch in word):
    					#print word, 'contains a number'
    					word = re.sub(r'[^a-zA-Z]', ' ', word)
    					#print word
    					tempWord = word.split()
    					#print tempWord
    					for word in tempWord:
							if False and word in tempArray:
								#print 'Found a duplicate word'
								duplicate = duplicate + 1
							else:
								tempArray.append(word)
				else:
					if False and word in tempArray:
						#print 'Found a duplicate word'
						duplicate = duplicate + 1
					else:
						tempArray.append(word)
			elif re.match("[^a-zA-Z]", word):
				False
				#print word, 'is a number'

        # Print out the word list (if small enough) or at least the size
	if len(tempArray) < 100:
		print "Here is word list:", tempArray
	else:
		print "Total (non-unique) words found: ", len(tempArray)

	global size
	size = len(tempArray)*2
	
	# Run test on Hash 0
        if False:   # Make False to disable this test
                hashTable = ['0']*size
                startTime = int(round(time.time() * 1000))
                #print startTime #test code
                runTest(tempArray, hashTable, hash0)
                endTime = int(round(time.time() * 1000))
                #print endTime #testcode
                addTime = endTime - startTime
                print "Hash0:", addTime, "milliseconds"

	# Run test on Hash A
        if False:
                hashTable = ['0']*size
                startTime = int(round(time.time() * 1000))
                #print startTime #test code
                runTest(tempArray, hashTable, hashA)
                endTime = int(round(time.time() * 1000))
                #print endTime #testcode
                addTime = endTime - startTime
                print "HashA:", addTime, "milliseconds"

	# Run test on Hash B
        if False:
                hashTable = ['0']*size
                startTime = int(round(time.time() * 1000))
                #print startTime #test code
                runTest(tempArray, hashTable, hashB)
                endTime = int(round(time.time() * 1000))
                #print endTime #testcode
                addTime = endTime - startTime
                print "HashB:", addTime, "milliseconds"

	# Run test on Hash C
        if False:
                hashTable = ['0']*size
                startTime = int(round(time.time() * 1000))
                #print startTime #test code
                runTest(tempArray, hashTable, hashC)
                endTime = int(round(time.time() * 1000))
                #print endTime #testcode
                addTime = endTime - startTime
                print "HashC:", addTime, "milliseconds"
                #print hashTable

	# Run test on Hash D
        if False:
                hashTable = ['0']*size
                startTime = int(round(time.time() * 1000))
                #print startTime #test code
                runTest(tempArray, hashTable, hashD)
                endTime = int(round(time.time() * 1000))
                #print endTime #testcode
                addTime = endTime - startTime
                print "HashD:", addTime, "milliseconds"
                #print hashTable

    # Run test on Hash E
        if False:
                hashTable = ['0']*size
                startTime = int(round(time.time() * 1000))
                #print startTime #test code
                runTest(tempArray, hashTable, hashE)
                endTime = int(round(time.time() * 1000))
                #print endTime #testcode
                addTime = endTime - startTime
                print "HashE:", addTime, "milliseconds"
                #print hashTable

    # Run test on Hash F
        if False:
                hashTable = ['0']*size
                startTime = int(round(time.time() * 1000))
                #print startTime #test code
                runTest(tempArray, hashTable, hashF)
                endTime = int(round(time.time() * 1000))
                #print endTime #testcode
                addTime = endTime - startTime
                print "HashF:", addTime, "milliseconds"
                #print hashTable