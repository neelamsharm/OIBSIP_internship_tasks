import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser
import wikipedia
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
        current_time = datetime.datetime.now()
        hour = current_time.hour
        if 0 <= hour < 12:
            speak("Good morning!")
        elif 12 <= hour < 18:
            speak("Good afternoon!")
        else:
            speak("Good evening!")
        speak("hello! i am nova how can i assist you today?")
            
greetme()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        text = r.recognize_google(audio, language='en-IN')
        text = text.lower()
        print(f"You said: {text}\n")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

if __name__ == "__main__":
    while True:
        command_text = command()
        if "open browser" in command_text:
            speak("Opening web browser")
            webbrowser.open("https://www.google.com") 
            
        elif "open youtube" in command_text:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
            
        elif "wikipedia" in command_text:
            speak("searching wikipedia for.....")
            command_text=command_text.replace("wikipidia","")
            content= wikipedia.summary(command_text,sentences=3)
            speak("According to wikipedia...")
            print(content)
            speak(content)
            
        elif "tell me the time" in command_text:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
            print(current_time)
            
        elif "open notepad" in command_text:
            speak("opening notepad...")
            os.startfile("notepad.exe")
            
        elif "open desktop"in command_text:
            speak("opening desktop...")
            os.startfile("C:\\Users\\amit sharma\\Desktop")
        
        elif "stop" in command_text:
            speak("Thank you for using Nova. Have a great day!")
            break
            
        else:
            speak("Sorry, I didn't understand that. Please try again.")