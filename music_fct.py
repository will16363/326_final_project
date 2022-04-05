from pygame import mixer

def music(music_file):
	with open (music_file, 'r', encoding='utf-8') as f:
		mixer.music.load(music_file)
		mixer.music.play(-1)	