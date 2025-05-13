import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
import tempfile

# Function to extract text from PDF and play as audiobook
def play_audiobook(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    
    full_text = ""
    for num in range(num_pages):
        page = pdf_reader.pages[num]
        data = page.extract_text()
        st.write(f"Extracting text from page {num + 1} of {num_pages}")
        full_text += data + " "

    st.write("Generating audio...")

    # Convert text to audio using gTTS
    tts = gTTS(text=full_text, lang='en')
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        st.audio(tmp.name, format='audio/mp3')

# Streamlit app UI
st.title("📖 Create Audiobook from PDF")
st.write("Upload an English PDF file to convert it into an audiobook.")

# File uploader
pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

# Button to generate audiobook
if pdf_file is not None:
    st.write(f"✅ File '{pdf_file.name}' uploaded successfully.")
    if st.button("▶️ Play Audiobook"):
        play_audiobook(pdf_file)
