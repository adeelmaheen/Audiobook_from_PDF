import pyttsx3
from PyPDF2 import PdfReader  # Change this import to PdfReader

book = open('demo.pdf', 'rb')
pdf_reader = PdfReader(book)  # Change PdfFileReader to PdfReader
num_pages = len(pdf_reader.pages)  # Use len(pdf_reader.pages) instead of pdf_reader.numPages

play = pyttsx3.init()
print('Playing Audio Book')

for num in range(0, num_pages):
    page = pdf_reader.pages[num]  # Access pages using pdf_reader.pages[num]
    data = page.extract_text()  # Use extract_text() instead of extractText()

    play.say(data)
    play.runAndWait()
