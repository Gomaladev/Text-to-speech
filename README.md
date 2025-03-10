#PDF to Speech Converter

**Overview**
   This project is a Streamlit-based web application that allows users to upload a PDF file, extract its text content, and convert the extracted text into speech using the gTTS (Google Text-to-Speech) API. The generated audio can be played directly within the application and downloaded for offline use.

**Features**
Upload a PDF file.
Extract text from the uploaded PDF.
Display the extracted text in a text area.
Convert the extracted text into speech using gTTS.
Play the generated audio file within the application.
Provide a download link for the generated audio file.

**Technologies Used**
Python
Streamlit (for the web interface)
pdfplumber (for text extraction from PDF)
gTTS (for text-to-speech conversion)

**Installation**
To run this project, you need to install the required dependencies. You can do so by running:

 _pip install streamlit pdfplumber gtts_

**Usage**
Run the Streamlit application using the following command:

_streamlit run app.py_

**Steps to Use:**
Upload a PDF file.
View the extracted text.
Click on Convert to Speech to generate the audio.
Play the generated speech.
Download the generated audio file if needed.

**File Structure**
_|-- app.py  # Main application script
|-- README.md  # Project documentation_

**Notes**
The application supports English text only for speech conversion.
The extracted text quality depends on the PDF's formatting.

**License**
This project is licensed under the MIT License.
