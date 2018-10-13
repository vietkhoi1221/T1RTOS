import speech_recognition
from pygame import mixer
from gtts import gTTS
import time
def say(text):
    source_file = "voice.mp3"
    tts = gTTS(text=text, lang='vi', slow = False)
    tts.save(source_file)
    mixer.init()
    mixer.music.load(source_file)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    time.sleep(1)
    mixer.music.load("tam.mp3")

speech_identifier = speech_recognition.Recognizer()

def phrase():
    with speech_recognition.Microphone() as source:
            speech_identifier.adjust_for_ambient_noise(source)
            audio = speech_identifier.listen(source)
    try:
            return speech_identifier.recognize_google(audio,language='vi')
    except speech_recognition.UnknownValueError:
            print("Đang chờ sếp ra lệnh.")
    return ""