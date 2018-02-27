#pip install gTTS

from gtts import gTTS
tts = gTTS(text='Hello', lang='en')
tts.save("hello.mp3")
