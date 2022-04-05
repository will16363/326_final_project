from pygame import mixer

def music(music_file):
	mixer.music.load(music_file)
	mixer.music.play(-1)