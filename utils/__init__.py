# ============================================
# __init__.py
# This file makes the utils folder a Python
# "package" — meaning other files can import
# from it easily.
#
# Instead of writing this everywhere:
#   from utils.chat_handler import init_model
#   from utils.storage import save_chat
#   from utils.image_generator import generate_image
#
# Any file can now just write:
#   from utils import init_model, save_chat, generate_image
#
# Think of this as a SHORTCUT connector between
# all the files inside the utils folder.
# ============================================


# ── Import everything from chat_handler.py ──
# These functions handle connecting to Gemini AI
from .chat_handler import (
    init_model,      # Connects to Gemini using API key
    start_chat,      # Starts a new conversation session
    send_message,    # Sends user message, gets AI reply
    get_history      # Extracts chat history for saving
)

# ── Import everything from storage.py ───────
# These functions handle saving/loading chats locally
from .storage import (
    save_chat,       # Saves current chat to a JSON file
    load_all_chats,  # Loads ALL saved chats from my_chats folder
    load_chat,       # Loads ONE specific saved chat
    delete_chat      # Deletes a saved chat file
)

# ── Import everything from image_generator.py
# This function handles generating images
from .image_generator import (
    generate_image   # Generates an image from a text prompt
)




# ## 🧠 What This File Does — Simple Explanation
#   This file makes it easy to import functions from all the utils files:
# utils/
# ├── chat_handler.py    ─┐
# ├── storage.py          ├──→  __init__.py  ──→  app.py can 
# └── image_generator.py ─┘                       import all 
#                                                  from one place