class Song(object):

	def __init__(self, lyrics, artist):
		self.lyrics = lyrics
		self.artist = artist

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there"],"?")

bull_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"], "?")

freshmen = Song(["For the life of me,",
				"I cannot remember",
				"what made us think we were wise",
				"and would never compromise"],"The Verve Pipe")

happy_bday.sing_me_a_song()
freshmen.sing_me_a_song()

mest_lyrics = ["Top down, seat back,",
				"Rollin in my cadillac"]

mest = Song(mest_lyrics, "Mest")
mest.sing_me_a_song()
print(mest.artist)