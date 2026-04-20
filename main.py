from speaker import speak
from listener import listen
from brain import askk_ai
from skills import search_google,search_youtube,play_my_song,play_song


sleep_mode = False
def main():
    global sleep_mode
    
    speak("Hello V")
    while True:
        
        if sleep_mode:
            command = listen(silent=True)
            if "friday" in command or "wake up" in command:
                speak("Yes boss,I am awake")
                sleep_mode =False
            continue
        
        command =listen()
        print("Command received:",command)

        if "sleep" in command:
            speak("Going to sleep. Call me when you need me")
            sleep_mode = True
            continue
        
        elif "stop" in command or "exit" in command:
            speak("Goodbye V")
            break
        
        elif "search" in command or "find" in command or "google" in command:
            speak("Searching for you")
            search_google(command.replace("search",""))
            
        elif "youtube" in command:
            speak("Searching Youtube")
            search_youtube(command.replace("youtube",""))
        
        elif "play my song" in command or "play my" in command or "my song" in command:
            speak("Playing your song")
            play_my_song()
            sleep_mode=True
        else:
            response = askk_ai(command)
            speak(response)
        

if __name__ == "__main__":
    main()
