import speech_recognition as speechRecognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = speechRecognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[39].id)


def talk_speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with speechRecognition.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk_speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk_speak('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk_speak(info)
    elif 'joke' in command:
        talk_speak(pyjokes.get_joke())
    else:
        talk_speak('Please say the command again.')


while True:
    run_alexa()
