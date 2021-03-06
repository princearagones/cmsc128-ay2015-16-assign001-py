# Author : Prince Karlo C. Aragones
# Description : Assignment in CMSC 128
#			create a library in 

def numToWords(number): #converts number to words, gets the place value by / and gets remaining digit with %
	string = ""
	if number == 0: #special case for zero to be printed
		string = unit(number)
	if number/1000000 != 0: #gets millions place
		string += unit(number/1000000) + " million"
		number = number%1000000

	if number/1000 !=0: #gets thousands place, then converts hundred thousands to thousands
		if number/100000 != 0: #gets the hundred thousands place
			string += " "+ unit(number/100000) + " hundred"
			number = number%100000
		if number/10000 != 0: #gets the ten thousands place
			string += " "+ tens (number/10000 * 10)
			number = number%10000
		if number/1000 != 0: #gets the thousands place
			string += " "+unit (number/1000)
			number = number%1000
		string += " thousand"
	if number/100 != 0: #gets hundreds place
		string += " "+ unit(number/100) + " hundred"
		number = number%100 #gets tens place
	if number/10 != 0 and number>20:
		string += " "+ tens (number/10 * 10)
		number = number%10 #gets ones place
	if number != 0:
		string += " "+ unit (number)

	return string

def wordsToNum(word): #converts words to numbers	
	number = 0
	if word.strip() != "":
		tok = word.split("million")
		if len(tok) == 2:
			number += convertToWord(tok[0].strip()) * 1000000
			word = tok[1]
			tok.pop()
		tok = word.split("thousand")
		if len(tok) == 2:
			number += (wordsToNum(tok[0].strip()) * 1000)
			word = tok[1]
			tok.pop()
		tok = word.split("hundred")
		if len(tok) == 2:
			number += convertToWord(tok[0].strip()) * 100
			word = tok[1]
			tok.pop()
		tok = word.split("ninety")
		if len(tok) == 2:
			number += 90
			word = tok[1]
			tok.pop()
		tok = word.split("eighty")
		if len(tok) == 2:
			number += 80
			word = tok[1]
			tok.pop()
		tok = word.split("seventy")
		if len(tok) == 2:
			number += 70
			word = tok[1]
			tok.pop()
		tok = word.split("sixty")
		if len(tok) == 2:
			number += 60
			word = tok[1]
			tok.pop()
		tok = word.split("fifty")
		if len(tok) == 2:
			number += 50
			word = tok[1]
			tok.pop()
		tok = word.split("fourty")
		if len(tok) == 2:
			number += 40
			word = tok[1]
			tok.pop()
		tok = word.split("thirty")
		if len(tok) == 2:
			number += 30
			word = tok[1]
			tok.pop()
		tok = word.split("twenty")
		if len(tok) == 2:
			number += 20
			word = tok[1]
			tok.pop()
		if word.strip() != "":
			number += convertToWord(word.strip())
			word = ""
	else:
		return "invalid input: empty string"
	return number

def convertToWord(word):
	if word == "zero":
		return 0
	elif word == "one":
		return 1
	elif word == "two":
		return 2
	elif word == "three":
		return 3
	elif word == "four":
		return 4
	elif word == "five":
		return 5
	elif word == "six":
		return 6
	elif word == "seven":
		return 7
	elif word == "eight":
		return 8
	elif word == "nine":
		return 9
	elif word == "ten":
		return 10
	elif word == "eleven":
		return 11
	elif word == "twelve":
		return 12
	elif word == "thirteen":
		return 13
	elif word == "fourteen":
		return 14
	elif word == "fifteen":
		return 15
	elif word == "sixteen":
		return 16
	elif word == "seventeen":
		return 17
	elif word == "eithteen":
		return 18
	elif word == "nineteen":
		return 19
	else:
		return -1

def tens(num):
	if num < 20:
		return unit(num)
	elif num == 50:
		return "fifty"
	elif num == 20:
		return "twenty"
	elif num == 30:
		return "thirty"
	else:
		string = unit(num/10) + "ty"
		return string

def unit(num):
	if num == 0:
		return "zero"
	elif num == 1:
		return "one"
	elif num == 2:
		return "two"
	elif num == 3:
		return "three"
	elif num == 4:
		return "four"
	elif num == 5:
		return "five"
	elif num == 6:
		return "six"
	elif num == 7:
		return "seven"
	elif num == 8:
		return "eight"
	elif num == 9:
		return "nine"
	elif num == 10:
		return "ten"
	elif num == 11:
		return "eleven"
	elif num == 12:
		return "twelve"
	elif num == 13:
		return "thirteen"
	elif num == 14:
		return "fourteen"
	elif num == 15:
		return "fifteen"
	elif num == 16:
		return "sixteen"
	elif num == 17:
		return "seventeen"
	elif num == 18:
		return "eithteen"
	elif num == 19:
		return "nineteen"
	else:
		return ""

def wordsToCurrency(word, cur):
	if cur in {"USD", "JPY", "PHP"}: #checks if its a valid currency
		return cur + str(wordsToNum(word)) #concatenates two strings
	else:
		return "Invalid currency"

def numberDelimited(number, char, jumps):
	string = str(number) #converts the number to string for easier manipulation
	output = ""
	length = len(string)
	jumpcounter = jumps
	while length != 0 and jumpcounter !=0:
		output = string[length-1] + output #gets the last char of the string
		length-=1
		jumpcounter-=1
		if jumpcounter == 0:
			output = char + output
			jumpcounter = jumps
			continue
	return output


#choice = 0
#while choice != 5:
#	print "---------M E N U --------------"
#	print "[1] Number to words"
#	print "[2] Words to number"
#	print "[3] Words to currency"
#	print "[4] Number delimited"
#	print "[5] Exit"
#	choice = input ("Choice: ")

#	if choice == 1:
#		number = input("Enter number: ")
#		numToWords(number)
#	if choice == 2:
#		word = raw_input("Enter word: ")
#		wordsToNum(word)
#	if choice == 3:
#		wordsToNum()
#	if choice == 4:
#		number = input("Enter number: ")
#		char = raw_input("Enter Char: ")
#		jumps = input("Enter jumps(number): ")
#		numberDelimited(number,char,jumps)
