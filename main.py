import speech_recognition as sr

def main():
    voiceInput = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something: ")
        audio = voiceInput.listen(source)
        try:
            text = voiceInput.recognize_google(audio)
            print("You said: " + text)
            if(text.contains("hello")):
                print("Hello")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()