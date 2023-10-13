import speech_recognition as sr
from logger import log_info, log_error

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            log_info("Listening for a command...")
            audio_data = recognizer.listen(source)
        
        command = recognizer.recognize_google(audio_data).lower()
        log_info(f"Recognized command: {command}")
        return command

    except sr.UnknownValueError:
        log_error("Could not understand the audio.")
        return None
    except sr.RequestError as e:
        log_error(f"Could not request results; check your network connection. Error: {e}")
        return None
