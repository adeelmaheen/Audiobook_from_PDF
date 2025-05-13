import streamlit as st
from gtts import gTTS
import os

# Function to generate and save audio
def generate_audio(text):
    tts = gTTS(text=text, lang='ur')  # 'ur' for Urdu
    tts.save("audio_output.mp3")
    return "audio_output.mp3"

# Streamlit UI
st.title("Urdu Text to Speech")

# User input for text
input_text = st.text_area("Enter Text in Urdu")

# Play audio button
if st.button("Play Audio"):
    if input_text:
        audio_file = generate_audio(input_text)  # Generate audio file
        st.audio(audio_file, format="audio/mp3")  # Play the audio
    else:
        st.warning("Please enter some text first.")
