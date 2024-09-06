# Text-to-Speech Application

A web application that allows users to upload PDF files, extract text, and convert it to speech. Built using Python and Streamlit, this app provides a seamless interface for converting PDF documents into audio files.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Streamlit App](#running-the-streamlit-app)
  - [Uploading a PDF](#uploading-a-pdf)
  - [Converting to Speech](#converting-to-speech)
  - [Logging Out](#logging-out)
- [Directory Structure](#directory-structure)
- [Project Files](#project-files)
- [License](#license)

## Overview
The PDF-to-Speech application provides functionality to convert PDF files into spoken audio. Users can upload PDF documents, extract the text content, and generate an audio file in MP3 format. This application is built with Streamlit for a user-friendly web interface.

## Features
- **PDF Upload:** Upload and select PDF files from your local device.
- **Text Extraction:** Extract text content from the uploaded PDF files.
- **Text-to-Speech Conversion:** Convert the extracted text into speech using the gTTS (Google Text-to-Speech) library.
- **Downloadable Audio:** Generate and download MP3 audio files of the converted speech.
- **User Authentication:** Includes login and signup functionalities for user management.

## Prerequisites
Ensure you have the following installed before using this application:
- Python 3.9+
- Streamlit
- gTTS
- PyPDF2
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Srishti-K-P/Text-to-speech-conversion.git
   cd pdf-to-speech-app
   ```
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Add Environment Variables**
   You might need to configure environment variables (e.g., paths for saving logs) if necessary.

## Usage

### Running the Streamlit App

  To launch the Streamlit application:
  ```bash
  streamlit run app.py
  ```
  The application will open in your default web browser.
  
### Uploading a PDF

  1. Navigate to the upload section of the app.
  2. Click the "Upload PDF" button and select your PDF file.
  3. The text will be extracted and displayed on the interface.

### Converting to Speech

  1. After uploading the PDF and extracting the text, click the "Convert to Speech" button.
  2. The text will be converted into an audio file.
  3. Download the generated MP3 file using the provided download link.

### Logging Out

  1. Click on the "Logout" button to end your session.
  2. You will be redirected to the login page.

## Directory Structure

```plaintext
text-to-speech-app/
│
├── app.py                  # Main Streamlit application
├── auth.py                 # Handles user authentication
├── extract_text.py         # Extracts text from PDF files
├── text_to_speech.py       # Converts text to speech
├── requirements.txt        # Lists Python dependencies
└── README.md               # Project documentation
```

## Project Files

- app.py :
Integrates the user interface for login, PDF upload, text extraction, and text-to-speech conversion.

- auth.py :
Manages user authentication including login, sign-up, and logout functionalities.

- extract_text.py :
Contains the logic for extracting text from uploaded PDF files.

- text_to_speech.py :
Handles the conversion of extracted text into speech using gTTS.

- requirements.txt :
Lists all necessary Python packages and versions for the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.







  


