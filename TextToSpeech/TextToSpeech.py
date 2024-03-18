#https://thepythoncode.com/article/convert-text-to-speech-in-python
import gtts
from playsound import playsound

# make request to google to get synthesis
tts = gtts.gTTS("this is a text to speech test")

# save the audio file
tts.save("hello.mp3")

# play the audio file
playsound("hello.mp3")