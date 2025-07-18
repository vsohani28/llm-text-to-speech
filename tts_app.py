
import streamlit as st
from gtts import gTTS
import os

st.title("🎤 Text to Speech Generator")
text = st.text_area("Enter text:", "Hello, this is a TTS demo!")

if st.button("Generate Speech"):
    tts = gTTS(text)
    tts.save("output/tts_streamlit.mp3")
    audio_file = open("output/tts_streamlit.mp3", "rb")
    st.audio(audio_file.read(), format='audio/mp3')
    st.success("Audio generated successfully!")
