import speech_recognition as sr
from pydub import AudioSegment
def convert_audio_to_wav(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    wav_file_path = "converted_audio.wav"
    audio.export(wav_file_path, format="wav")
    return wav_file_path
def transcribe_audio(audio_file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
    
    # Recognize speech using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Google Web Speech API could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"
if __name__ == "__main__":
    # Replace 'your_audio_file.mp3' with the path to your audio file
    main("your_audio_file.mp3")