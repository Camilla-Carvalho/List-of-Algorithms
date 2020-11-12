from gtts import gTTS
from playsound import playsound

def play_audio(path of audio)

    playsound('/path/to/a/sound/file/you/want/to/play.mp3')

def convert_to_audio(text):
    my_audio = gTTS(text)
    my_audio.save('df021.mp3')
    play_audio('df021.mp3')

convert_to_audio('...')