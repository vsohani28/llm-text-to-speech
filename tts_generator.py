
import pyttsx3

text = input("Enter text to convert to speech: ")

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

engine.say(text)
engine.save_to_file(text, 'output/tts_output.mp3')
engine.runAndWait()

print("✅ Speech saved to output/tts_output.mp3")
