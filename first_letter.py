#def first_letter(reply):
#	reply = str(reply)
#	reply = reply[:1]
#	return (reply)

#def first_character(reply):
#	reply = str(reply[0])
#	return(reply)

#def is_Vowel(reply):
#	if reply == 'a' or reply == 'A' or reply == 'e' or reply == 'E' or reply == 'i' or reply == 'I' or reply =='o' or reply =='O' or reply == 'u' or reply == 'U':
#		return True
#	else:
#		return False

def is_Vowel_two(reply):
	return reply.lower() in 'aeiou'

reply = input("Please enter your word:")
print(is_Vowel(reply))

