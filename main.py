import pyttsx3
import datetime
import speechRecognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print(voices[0].id)

def hearQuery():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 5:
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")

    

if __name__ == '__main__':
    speak("I am inevitable")
