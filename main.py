import streamlit as st
import pyttsx3
from PyPDF2 import PdfReader

# Function to extract text from the PDF and play as audiobook
def play_audiobook(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    play = pyttsx3.init()
    st.write('Playing Audiobook...')

    for num in range(0, num_pages):
        page = pdf_reader.pages[num]
        data = page.extract_text()

        # Use Streamlit to display the current page being read
        st.write(f"Reading page {num + 1} of {num_pages}")
        play.say(data)
        play.runAndWait()

# Streamlit app interface
st.title("Create AudioBook from PDF")
st.write("Upload a PDF file to create an audiobook.")

# File uploader for PDF
pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

# If a file is uploaded, proceed with the audiobook conversion
if pdf_file is not None:
    # Display file name
    st.write(f"File '{pdf_file.name}' uploaded successfully!")

    # Button to start playing the audiobook
    if st.button('Play Audiobook'):
        play_audiobook(pdf_file)
