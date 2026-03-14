# ============================================
# chat_handler.py
# This is the BRAIN of our chatbot.
# It connects to Gemini AI and handles all
# conversations.
# ============================================

import google.generativeai as genai 
import os
from dotenv import load_dotenv

# Load the API key from our .env file
load_dotenv()


# ─────────────────────────────────────────────
# FUNCTION 1: Connect to Gemini AI
# ─────────────────────────────────────────────
def init_model():
    # Read the API key from .env file
    api_key = os.getenv("GEMINI_API_KEY")

    # Stop if no API key found
    if not api_key:
        raise ValueError(
            "❌ API Key not found! "
            "Please check your .env file."
        )

    # Connect to Gemini using our API key
    genai.configure(api_key=api_key)

    # Instructions that tell Gemini how to behave
    system_prompt = """
    You are INO, a friendly and highly capable AI assistant.

    Your abilities:
    1. Answer any question clearly and in simple language.
    2. Write code in any programming language when asked.
       - Always put code inside triple backticks like ```python
       - Always explain what the code does after writing it
       - Always add comments inside the code
    3. Help with analysis, writing, math, and problem solving.

    Rules:
    - Be friendly and encouraging
    - Keep answers clear and easy to understand
    - If you dont know something, say so honestly
    """

    # Create and return the Gemini model
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=system_prompt
    )

    return model


# ─────────────────────────────────────────────
# FUNCTION 2: Start a New Chat Session
# ─────────────────────────────────────────────
def start_chat(model):
    # Start a fresh conversation with empty history
    chat_session = model.start_chat(history=[])
    return chat_session


# ─────────────────────────────────────────────
# FUNCTION 3: Send a Message, Get a Reply
# ─────────────────────────────────────────────
def send_message(chat_session, user_message):
    # Send message to Gemini and return the reply
    response = chat_session.send_message(user_message)
    return response.text


# ─────────────────────────────────────────────
# FUNCTION 4: Get Chat History for Saving
# ─────────────────────────────────────────────
def get_history(chat_session):
    messages = []

    # Loop through every message in the conversation
    for turn in chat_session.history:

        # Rename "user" to "you" and "model" to "bot"
        if turn.role == "user":
            role = "you"
        else:
            role = "bot"

        # Get the text of this message
        text = turn.parts[0].text if turn.parts else ""

        # Add to our messages list
        messages.append({
            "role": role,
            "message": text
        })

    return messages