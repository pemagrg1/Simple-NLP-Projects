#pip install gTTS

from gtts import gTTS
myobj = gTTS(text="Hello world!", lang='en', slow=False)
myobj.save("welcome.mp3")
