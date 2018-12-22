reply = str(input("Please enter a word:  "))

def is_Vowel(reply):
	return reply.lower() in 'aeiou'

def has_Vowels(reply):
	reply = reply.lower()
	for i in reply:
		if is_Vowel(i) == True:
			return True
	return False 

print(has_Vowels(reply))
