import pyttsx3
import PyPDF2

book = open('MNSC.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)
print(reader.numPages)
# # reader.pages[0]    # do not use this before decrypt
# if reader.isEncrypted:
#     reader.decrypt('')
# reader.pages[0]
# page = pdfReader.getPage(5)
# text = page.extract_text()

# engine = pyttsx3.init()
# engine.say(text)
# engine.runAndWait()