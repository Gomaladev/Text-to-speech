import streamlit as st
import pdfplumber
from gtts import gTTS
import os

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as file:
        text = ''
        for page in file.pages:
            text += page.extract_text() + '\n'
    return text

def text_to_speech(text, output_path):
    tts = gTTS(text, lang='en')
    tts.save(output_path)

def main():
    st.title("PDF to Speech Converter")
    
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        
        text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Text", text, height=300)
        
        if st.button("Convert to Speech"):
            output_audio = "Audio.mp3"
            text_to_speech(text, output_audio)
            st.audio(output_audio, format='output_audio.mp3')
            
            # Provide a download link
            with open(output_audio, "rb") as f:
                st.download_button("Download Audio", f, file_name=output_audio, mime="audio/mp3")

if __name__ == "__main__":
    main()
