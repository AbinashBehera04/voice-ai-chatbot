from speech import speak
from listener import takeCommand
from commands import wishMe, getTime
from automation import *
from wiki_search import search_wikipedia
from notes_manager import *

import pyjokes

speak(wishMe())
speak("I am your voice assistant.")
failure_count = 0
while True:

    command = takeCommand()
    # command = input("Enter command: ").lower()


    if command == "":

        failure_count += 1

        if failure_count >= 5:
            speak("Microphone problem detected")
            break

        continue

    failure_count = 0








    # Websites

    if "google" in command:
        speak("Opening Google")
        open_google()

    elif "youtube" in command:
        speak("Opening YouTube")
        open_youtube()

    elif "github" in command:
        speak("Opening GitHub")
        open_github()

    # Time

    elif "time" in command:
        speak(f"The time is {getTime()}")

    # Wikipedia

    elif "wikipedia" in command:

        topic = command.replace("wikipedia", "")

        result = search_wikipedia(topic)

        speak(result)

    # Notes

    elif "save note" in command:

        note = command.replace("save note", "")

        save_note(note)

        speak("Note saved")

    elif "read notes" in command:

        notes = read_notes()

        speak(notes)

    # Todo

    elif "add task" in command:

        task = command.replace("add task", "")

        add_task(task)

        speak("Task added")

    elif "show tasks" in command:

        tasks = show_tasks()

        speak(tasks)

    # Joke

    elif "joke" in command:

        speak(pyjokes.get_joke())

    # System Commands

    elif "shutdown" in command:

        speak("Shutting down in one minute")

        shutdown_pc()

    elif "restart" in command:

        speak("Restarting in one minute")

        restart_pc()

    elif "lock computer" in command:

        speak("Locking computer")

        lock_pc()
    #Battery   
     
    elif "battery" in command:

        speak(battery_status())
    #screenshot
    elif "screenshot" in command:

        take_screenshot()

        speak("Screenshot saved")
    #photo
    elif "take photo" in command:

        take_photo()

        speak("Photo captured successfully")

    elif "hello" in command:
        speak("Hello Abinash")

    elif "how are you" in command:
        speak("I am fine. Thank you for asking.")

    elif "your name" in command:
        speak("I am your voice assistant.")
        
    # Exit

    elif "exit" in command or "goodbye" in command:

        speak("Goodbye Abinash")

        break

    else:

        speak("I did not understand that command.")

        