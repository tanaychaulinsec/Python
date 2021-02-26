import pyttsx3
import PyPDF2
book=open(r'C:\Users\1434743\Project\Splitwise\models\grok_system_design_interview.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages

speaker=pyttsx3.init()
for num in range(1,pages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()