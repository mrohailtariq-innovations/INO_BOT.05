# ============================================
# storage.py
# This file handles saving and loading chats
# to/from your local computer as JSON files.
# Every chat is saved inside the my_chats folder
# ============================================

import json        # json helps us save data in a readable file format
import os          # os helps us create folders and work with file paths
from datetime import datetime  # datetime gives us the current date and time


# This is the folder where all chats will be saved
CHATS_FOLDER = "my_chats"


# ─────────────────────────────────────────────
# FUNCTION 1: Save a chat to a file
# ─────────────────────────────────────────────
def save_chat(messages):
    """
    Takes the chat messages and saves them as a JSON file.
    The file is named using the current date and time
    so each file has a unique name.
    Example filename: chat_2026-03-08_10-30-00.json
    """

    # Create the my_chats folder if it doesn't exist yet
    os.makedirs(CHATS_FOLDER, exist_ok=True)

    # Get the current date and time for the filename
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")  # e.g. 2026-03-08_10-30-00
    filename = f"chat_{timestamp}.json"             # e.g. chat_2026-03-08_10-30-00.json

    # Full path where the file will be saved
    filepath = os.path.join(CHATS_FOLDER, filename)

    # This is the data we will save inside the file
    chat_data = {
        "title": f"Chat on {now.strftime('%B %d, %Y at %I:%M %p')}",  # Human readable title
        "date": now.strftime("%Y-%m-%d"),   # Just the date
        "time": now.strftime("%H:%M:%S"),   # Just the time
        "messages": messages                 # The actual chat messages
    }

    # Open the file and write the data as JSON
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(chat_data, file, indent=2, ensure_ascii=False)
        # indent=2 makes the file human-readable (nicely formatted)

    return filepath  # Return the path so we can tell the user where it was saved


# ─────────────────────────────────────────────
# FUNCTION 2: Load ALL saved chats
# ─────────────────────────────────────────────
def load_all_chats():
    """
    Reads all saved chat files from the my_chats folder
    and returns them as a list.
    Used to show the list of past chats in the sidebar.
    """

    # If the folder doesn't exist yet, return empty list
    if not os.path.exists(CHATS_FOLDER):
        return []

    chats = []  # Empty list to collect all chats

    # Loop through every file in the my_chats folder
    for filename in sorted(os.listdir(CHATS_FOLDER), reverse=True):

        # Only process .json files
        if filename.endswith(".json"):
            filepath = os.path.join(CHATS_FOLDER, filename)

            # Open and read the file
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                data["filename"] = filename  # Add filename so we can reference it later
                chats.append(data)

    return chats  # Return the full list of chats


# ─────────────────────────────────────────────
# FUNCTION 3: Load ONE specific chat
# ─────────────────────────────────────────────
def load_chat(filename):
    """
    Loads a single chat file by its filename.
    Used when the user clicks on a past chat to view it.
    """

    filepath = os.path.join(CHATS_FOLDER, filename)

    # Check if file exists before trying to open it
    if not os.path.exists(filepath):
        return None  # Return nothing if file not found

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)  # Read and return the chat data


# ─────────────────────────────────────────────
# FUNCTION 4: Delete a saved chat
# ─────────────────────────────────────────────
def delete_chat(filename):
    """
    Deletes a specific chat file from the my_chats folder.
    Used when the user clicks the delete button on a saved chat.
    """

    filepath = os.path.join(CHATS_FOLDER, filename)

    # Only delete if the file actually exists
    if os.path.exists(filepath):
        os.remove(filepath)
        return True   # Deletion was successful

    return False  # File was not found


# ## 🧠 What This File Does — Simple Explanation
# This file has 4 main functions that let you save and manage your chats:
# save_chat()       → Saves your conversation to a .json file
# load_all_chats()  → Gets list of ALL your saved chats
# load_chat()       → Opens ONE specific saved chat
# delete_chat()     → Deletes a saved chat file---
