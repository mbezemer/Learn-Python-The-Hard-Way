class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

halleluja = Song(["Halleluja", "Halleluja", "Halleluja"])						
						
kapoentje = Song(["Sinterklaas Kapoentje", "Gooi wat in m'n schoentje", "Dank u Sinterklaasje"])

rock = Song(["We will", "We will...", "rock you!"])

wedding = Song(["Daar komt de bruid", "La la la"])

song_var = ["This is a song", "lalala a song", "tadaa!"]

music = Song(song_var)
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

halleluja.sing_me_a_song()

kapoentje.sing_me_a_song

rock.sing_me_a_song()

wedding.sing_me_a_song()

music.sing_me_a_song()