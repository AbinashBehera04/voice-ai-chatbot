import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

def takeCommand():

    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 1
    recognizer.energy_threshold = 300

    try:

        print("Listening... Speak now")

        duration = 8
        sample_rate = 16000

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='int16'
        )

        sd.wait()

        sf.write("temp.wav", recording, sample_rate)

        with sr.AudioFile("temp.wav") as source:

            audio = recognizer.record(source)

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.UnknownValueError:

        print("Could not understand the audio")
        return ""

    except sr.RequestError as e:

        print("Google API error:", e)
        return ""

    except Exception as e:

        print("Error:", e)
        return ""