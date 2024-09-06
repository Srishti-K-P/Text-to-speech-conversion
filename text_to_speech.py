from gtts import gTTS
import streamlit as st

def text_to_speech_gtts(text, output_audio_file):
    """
    Convert text to speech using gTTS (Google Text-to-Speech) and save it as an audio file.
    param:
        text (str): The text that needs to be converted to speech.
        output_audio_file (str): The path where the output audio file will be saved.
    return:
        bool: True if the conversion and saving process is successful, False otherwise.
    """
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_audio_file)
        return True
    except Exception as e:
        st.error(f"Error in converting text to speech: {e}")
        return False
