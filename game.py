two_plus_key_describe = "This room is round, with a KEY to your left, and a HOLE in the floor opposite of the door you just came through."
two_no_key_describe = "This room is round, with a HOLE in the floor at the far edge, opposite the door you just came through."


five_decribe = "When you enter this room, you notice that tiles on the floor seem to glow.\n On closer inspection, the flowing spots are actually lava.\n It looks like you'll have to navigate a safe path across."
six_describe = "Oh wow, is that daylight?\n You are blinded by the brightness of the sun, but happy with the knowledge you've escaped.\n THE END!"


roomnum = "one"
not_much = "That doesn't seem to do much in here."
flashlight = "off"

def flashlight_toggle():
	global flashlight
	if flashlight == "off":
		flashlight = "on"
		print ("Your flashlight is now on.")
	else:
		flashlight = "off"
		print ("You turn your flashlight off.")
	return ()

def get_response():
	user_input = input(">  ")
	user_input = user_input.upper()
	return user_input

def roomone():
	print("This room is mostly grey and empty.\nThere are doors to the NORTH and SOUTH.")
	response = get_response()
	if response == "LOOK":
		print("This room is mostly grey and empty.\nThere are doors to the NORTH and SOUTH.")
		roomone()
	elif response == "FLASHLIGHT":
		flashlight_toggle()
		print(not_much)
		roomone()
	elif response == "NORTH":
		print("You go through the door to the NORTH...")
		roomtwo()
	elif response == "SOUTH":
		print("You go through the door to the SOUTH...")
		roomfour()
	else:
		print("Please pick something possible to do.")
		roomone()
	return ()

def roomtwo():
	if flashlight == "on":
		print("The room is lit by your flashlight.\nYou can see that there is a door directly across from you, to the NORTH.\nThe door you came in through is to the SOUTH of you.")
	else:
		print("This room is crazy dark. You can't see much of anything.")
	response = get_response()
	if response == "LOOK":
		roomtwo()
	elif response == "FLASHLIGHT":
		flashlight_toggle()
		roomtwo()
	elif response == "NORTH":
		roomthree()
	elif response == "SOUTH":
		print("You go back through the door to the SOUTH...")
		roomone()
	else:
		print("That's not possible in this room.")
		roomtwo()
	return ()

def roomthree():
	print("The entirety of this room is taken up by a stone SPHINX.\n You can't see any other doors in this room other than the one to the SOUTH that you came in through,\n and the SPHINX seems to be watching you.")
	response = get_response()
	if response == "LOOK":
		roomthree()
	elif response == "FLASHLIGHT":
		flashlight_toggle()
		print("Doing that doesn't seem to do much, other than making the SPHINX squint at you, unamused.")
	elif response == "SOUTH":
		print("You go back through the door to the SOUTH...")
		roomtwo()
	elif response == "SPHINX":
		print("""
It turns it's head to look directly at you, grey stone eyes eerie.
There is a grinding sound as it opens it's mouth. 
From deep inside the beast comes a deep, rumbling voice, and it says:
"They are dark and on the run, without sun there will be none. What are they?"
It seems to wait for your response...
""")
		response = get_response()
		if response == "SHADOWS":
			print("The SPHINX nods and closes it's eyes.\nIt moves it's gigantic stone body to reveal a hole in the ground underneath it.\n One huge, heavy paw sweeps you effortlessly into the hole.")
			roomfive()
		else:
			print("The SPHINX grimaces and says nothing. It seems you've gotten the riddle wrong.\n")
			roomthree()
	else:
		print("That's not possible in this room.")
		roomthree()
	return()

has_key = "no"

def roomfour():
	global has_key
	if has_key == "no":
		print("This room is round, with a KEY to your left, and a HOLE in the floor.\n Behind you, to the NORTH, is the door you just came through.")
	else:
		print("This room is round, with a HOLE in the floor at the far edge, opposite the door you just came through, which is to the NORTH.")
	response = get_response()
	if response == "KEY":
		if has_key == "no":
			print("You pick up the key and put it safely in your pocket.")
			has_key = "yes"
			roomfour()
		else:
			print("The key is already in your pocket. You touch it just to be sure you didn't lose it.")
			roomfour()
	elif response == "HOLE":
		print ("You decide to jump down into the black abyss of the hole...")
		roomfive()
	elif response == "NORTH":
		print("You decide to go back NORTH through the door you came in through...")
		roomone()
	elif response == "FLASHLIGHT":
		flashlight_toggle()
		print("That doesn't seem to do much in here.")
		roomfour()
	else:
		print("That's not possible in this room.")
		roomfour()
	return()

def roomfive():
	print("Far above you is the hole in the ceiling that you came through.\nIn front of you, there is a door with a big, fancy LOCK.\nThere is also a door to the WEST.")
	response = get_response()
	if response == "LOCK":
		if has_key == "yes":
			print("You pull the key fron your pocket and slide it smoothly into the LOCK.\nIt falls off the door and the door swings open, releasing you.")
			print("\nCONGRATS! YOU HAVE ESCAPED!")
		else:
			print("You don't seem to have the KEY you need to unlock this.\nMaybe it's in another room?")
			roomfive()	
	elif response == "FLASHLIGHT":
		flashlight_toggle()
		print("That doesn't seem to do much in here.")
		roomfive()
	elif response == "WEST":
		print("You go through the door to the WEST. Once you step foot through it, it swings shut.\nIt blends in seamlessly and smoothly as part of the wall.")
		roomone()
	else:
		print("That doesn't look like it's possible in here.")
		roomfive()
	return()

print("""
You were abducted by tiny purple flower people and knocked unconcious.
When you wake up you find yourself in an unfamiliar place, with only a FLASHLIGHT.
LOOK around to figure out what to do.""")
roomone()



#def roomtwo(has_key,roomnum):
#	if has_key == true:
#		print(two_no_key_describe)
#	else:
#		print(two_plus_key_describe)
#	get_response()

#	if get_response == "KEY":
#		if has_key == true
#			print("You already have the key. See, there it is, right in your pocket.")
#		else:
#			has_key = true
#			print("You pick up the KEY and stash it safely in your pocket.")
#	elif get_response == "HOLE":
#		print ("You jump in the HOLE.\nThere is a loud wooshing sound as the wind passes your ears, and you fall a long distance.")
#		roomnum = five
#	elif get_response == "BACK"
#		print ("You turn around to go back into the room you just game from")
#		roomnum = one
#	else:
#		print("Please pick something possible to do.")