import os
import streamlit as st
from auth import signup_user, handle_login, logout_user
from extract_text import extract_text_from_pdf
from text_to_speech import text_to_speech_gtts


def show_initial_options():
    """
    Display the initial options for the user to either login or sign up.
    return: None
    """
    st.markdown("<h1 style='text-align: center; color: green;'>Welcome to PDF-to-Speech App</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:22px;'><br>Please choose an option to proceed:<br></h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Login", key="login_button"):
            st.session_state["show_login"] = True
            st.session_state["show_signup"] = False
            st.session_state["show_initial"] = False
    
    with col2:
        if st.button("Sign Up", key="signup_button"):
            st.session_state["show_login"] = False
            st.session_state["show_signup"] = True
            st.session_state["show_initial"] = False


def show_login_form():
    """
    Display the login form for users to enter their credentials.
    return: None
    """
    st.subheader("Login")
    
    username = st.text_input("Username", value="", key="login_username")
    password = st.text_input("Password", type="password", value="", key="login_password")
    
    if st.button("Login", key="login_form_button"):
        success, message = handle_login(username, password)
        if success:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["show_login"] = False
            st.session_state["show_signup"] = False
            st.session_state["pdf_upload"] = True
        else:
            st.error(message)


def show_signup_form():
    """
    Display the signup form for users to create a new account.
    return: None
    """
    st.subheader("Sign Up")
    
    new_username = st.text_input("New Username", value="", key="signup_username")
    new_password = st.text_input("New Password", type="password", value="", key="signup_password")
    
    if st.button("Sign Up", key="signup_form_button"):
        success, message = signup_user(new_username, new_password)
        if success:
            st.success(message)
            st.session_state["new_username"] = ""
            st.session_state["new_password"] = ""
            st.session_state["show_signup"] = False
            st.session_state["show_login"] = False
            st.session_state["show_initial"] = True
        else:
            st.error(message)

    if st.button("Back to Home", key="back_button"):
        st.session_state["show_signup"] = False
        st.session_state["show_login"] = False
        st.session_state["show_initial"] = True


def pdf_to_speech_ui():
    """
    Display the PDF-to-Speech interface for authenticated users to upload PDFs and convert them to speech.
    return: None
    """
    st.title(f"Hello, {st.session_state['username']}!")

    if st.sidebar.button("Logout", key="logout_button"):
        logout_user()

    st.write("Upload a PDF file, and we'll convert its text to speech!")

    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

    if pdf_file is not None:
        with open("output.pdf", "wb") as f:
            f.write(pdf_file.read())

        st.write("Extracting text from PDF...")
        text = extract_text_from_pdf("output.pdf")
        st.write(text)

        if text.strip():
            if st.button("Convert to Speech", key="convert_to_speech_button"):
                output_audio_file = "output.mp3"
                if text_to_speech_gtts(text, output_audio_file):
                    st.success("Conversion successful! Download your MP3 file below.")
                    st.audio(output_audio_file, format="audio/mp3")
                    with open(output_audio_file, "rb") as file:
                        st.download_button("Download MP3", data=file, file_name="output.mp3", mime="audio/mp3")
        else:
            st.warning("No text could be extracted from this PDF.")

        os.remove("output.pdf")


def logout_user():
    """
    Handle the user logout process and reset session state.
    return: None
    """
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["pdf_upload"] = False
    st.session_state["show_initial"] = True


def main():
    """
    Main function to initialize the app and determine which UI to display based on the session state.
    return: None
    """
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "show_initial" not in st.session_state:
        st.session_state["show_initial"] = True
    if "show_login" not in st.session_state:
        st.session_state["show_login"] = False
    if "show_signup" not in st.session_state:
        st.session_state["show_signup"] = False
    if "pdf_upload" not in st.session_state:
        st.session_state["pdf_upload"] = False

    # Determine which UI to show based on session state
    if st.session_state["logged_in"]:
        pdf_to_speech_ui()
    elif st.session_state["show_login"]:
        show_login_form()
    elif st.session_state["show_signup"]:
        show_signup_form()
    else:
        show_initial_options()

if __name__ == '__main__':
    main()
