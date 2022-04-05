from playsound import playsound
import glob

def play_music(path):
	"""This function plays music during the game.

	Args:
		path (str): Path to the music file.

	Side effects:
		Plays music throughout the game.
	"""
	for song in glob.glob(path):
		playsound(song)

play_music("music_file.mp3")