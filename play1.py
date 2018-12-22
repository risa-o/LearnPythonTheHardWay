def first_letter(reply):
	reply = str(reply)
	reply = reply[:1]
	return (reply)

reply = input("Please enter your word:")
print(first_letter(reply))