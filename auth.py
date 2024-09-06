import hashlib
import streamlit as st

# Simulated in-memory user "database" with pre-hashed passwords
users_db = {
    "user1": hashlib.sha256("qwertyuiop".encode()).hexdigest(),
    "admin": hashlib.sha256("admin".encode()).hexdigest()
}


def hash_password(password):
    """
    Hash a password using SHA-256.
    param:password (str): The plain text password to be hashed.
    return:str: The hashed password as a hexadecimal string.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def signup_user(username, password):
    """
    Register a new user with a hashed password.
    param:
        username (str): The username for the new user.
        password (str): The plain text password for the new user.
    return: tuple: A boolean indicating success, and a message string.
    """
    if username in users_db:
        return False, "Username already exists!"
    users_db[username] = hash_password(password)
    return True, "User signed up successfully!"


def login_user(username, password):
    """
    Authenticate a user by checking their username and password.
    param:
        username (str): The username of the user attempting to log in.
        password (str): The plain text password of the user.
    return: tuple: A boolean indicating success, and a message string.
    """
    if username in users_db and users_db[username] == hash_password(password):
        return True, "Login successful!"
    return False, "Invalid username or password!"


def is_user_logged_in():
    """
    Check if a user is currently logged in.
    return: bool: True if a user is logged in, False otherwise.
    """
    return st.session_state.get("logged_in", False)


def logout_user():
    """
    Log out the current user by clearing session state.
    return: None
    """
    st.session_state["logged_in"] = False
    st.session_state["username"] = None


def handle_login(username, password):
    """
    Handle the login process and manage session state.
    param:
        username (str): The username of the user attempting to log in.
        password (str): The plain text password of the user.
    return: tuple: A boolean indicating success, and a message string.
    """
    success, message = login_user(username, password)
    if success:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
    return success, message

