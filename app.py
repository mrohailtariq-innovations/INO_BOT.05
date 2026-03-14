# ============================================
# app.py
# This is the MAIN WEB UI of INO chatbot.
# Built using Streamlit — a Python library
# that turns Python code into a web app.
#
# How to run:
#   streamlit run app.py
#
# Features:
#   💬 Chat with Gemini AI
#   👨‍💻 Generate code
#   🎨 Generate images
#   💾 Save and load past chats
# ============================================

import streamlit as st   # Streamlit builds our web interface

# Import all our utility functions from the utils folder
from utils.chat_handler import init_model, start_chat, send_message, get_history
from utils.storage import save_chat, load_all_chats, load_chat, delete_chat
from utils.image_generator import generate_image


# ─────────────────────────────────────────────
# PAGE CONFIGURATION
# This must be the FIRST streamlit command
# It sets the browser tab title and layout
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="INO - AI Assistant",   # Browser tab title
    page_icon="🤖",                    # Browser tab icon
    layout="wide"                      # Use full width of the screen
)


# ─────────────────────────────────────────────
# SESSION STATE SETUP
# Streamlit reruns the entire file on every
# interaction. Session state lets us REMEMBER
# data between those reruns — like the chat
# history and the AI model connection.
# ─────────────────────────────────────────────

# Initialize the AI model ONCE when app first loads
# If it already exists in session, skip this step
if "model" not in st.session_state:
    st.session_state.model = init_model()
    # st.session_state is like a memory box that
    # keeps values alive across page reruns

# Initialize the chat session ONCE when app first loads
if "chat_session" not in st.session_state:
    st.session_state.chat_session = start_chat(st.session_state.model)

# Initialize empty messages list to store conversation
# Each message is a dict: {role, content, type}
if "messages" not in st.session_state:
    st.session_state.messages = []


# ─────────────────────────────────────────────
# SIDEBAR
# The left panel of the app
# Contains: New Chat, Save Chat, Past Chats
# ─────────────────────────────────────────────
with st.sidebar:

    # App title and description in sidebar
    st.title("🤖 INO.05  Assistant")
    st.caption("Powered by Google Gemini AI")
    st.markdown("---")  # Horizontal divider line

    # ── Button: Start New Chat ─────────────────
    if st.button("➕ New Chat", use_container_width=True):
        # Create a fresh chat session (clears memory)
        st.session_state.chat_session = start_chat(st.session_state.model)
        # Clear all messages from the screen
        st.session_state.messages = []
        # Rerun the app to refresh everything
        st.rerun()

    # ── Button: Save Current Chat ──────────────
    if st.button("💾 Save Chat", use_container_width=True):
        # Only save if there are actual messages
        if st.session_state.messages:
            # Get formatted history from the chat session
            history = get_history(st.session_state.chat_session)
            # Save to a JSON file in my_chats folder
            filepath = save_chat(history)
            # Show success message with file location
            st.success(f"✅ Chat saved!\n`{filepath}`")
        else:
            # Warn user if there's nothing to save
            st.warning("⚠️ Nothing to save yet!")

    st.markdown("---")

    # ── Past Chats Section ─────────────────────
    st.subheader("📂 Past Chats")

    # Load all saved chat files from my_chats folder
    saved_chats = load_all_chats()

    if not saved_chats:
        # Show message if no chats saved yet
        st.caption("No saved chats yet.")
    else:
        # Loop through each saved chat and show it as a button
        for chat in saved_chats:

            # Two columns: chat title button + delete button
            col1, col2 = st.columns([4, 1])

            with col1:
                # Show the chat title — truncate if too long
                title = chat["title"][:28] + "..." if len(chat["title"]) > 28 else chat["title"]

                # When clicked, load this chat into the screen
                if st.button(f"📄 {title}", key=chat["filename"], use_container_width=True):
                    # Load the full chat data from the file
                    loaded = load_chat(chat["filename"])
                    if loaded:
                        # Convert saved messages back into our format
                        st.session_state.messages = [
                            {
                                "role": m["role"],
                                "content": m["message"],
                                "type": "text"
                            }
                            for m in loaded["messages"]
                        ]
                        st.rerun()  # Refresh to show loaded messages

            with col2:
                # Delete button for this chat
                if st.button("🗑️", key=f"del_{chat['filename']}"):
                    delete_chat(chat["filename"])
                    st.rerun()  # Refresh sidebar after deletion

    st.markdown("---")
    st.caption("Built with ❤️ using Gemini API")


# ─────────────────────────────────────────────
# MAIN CHAT AREA
# The right side — where the conversation shows
# ─────────────────────────────────────────────
st.title("💬 INO — Your AI Assistant")
st.caption("Chat · Write Code · Generate Images · Save Conversations")
st.markdown("---")


# ── Display All Messages ───────────────────────
# Loop through all messages stored in session state
# and display them on screen in order
for msg in st.session_state.messages:

    # "user" role shows on the right side (your messages)
    # "assistant" role shows on the left (bot messages)
    if msg["role"] == "you":
        with st.chat_message("user"):
            st.markdown(msg["content"])

    else:
        with st.chat_message("assistant"):
            # If this message is an image, display the image
            if msg.get("type") == "image":
                st.image(msg["content"], caption="🎨 Generated Image")
            else:
                # Otherwise display as normal text/code
                st.markdown(msg["content"])


# ─────────────────────────────────────────────
# INPUT AREA
# At the bottom — where user types their message
# ─────────────────────────────────────────────

# Two columns: text input + image toggle switch
col1, col2 = st.columns([6, 1])

with col2:
    # Toggle switch to switch between chat and image mode
    image_mode = st.toggle("🎨 Image Mode", help="Turn ON to generate images instead of chatting")

with col1:
    # The chat input box at the bottom of the screen
    if image_mode:
        placeholder = "Describe the image you want... e.g. a dragon flying over a city"
    else:
        placeholder = "Ask me anything, request code, or just chat..."

    user_input = st.chat_input(placeholder)


# ─────────────────────────────────────────────
# HANDLE USER INPUT
# This runs every time the user sends a message
# ─────────────────────────────────────────────
if user_input:

    # ── Step 1: Show user message on screen ───
    st.session_state.messages.append({
        "role": "you",
        "content": user_input,
        "type": "text"
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ── Step 2: Image Generation Mode ─────────
    if image_mode:
        # User wants to generate an image
        with st.chat_message("assistant"):
            with st.spinner("🎨 Generating your image, please wait..."):
                try:
                    # Call our image generator with the user's prompt
                    filepath, image = generate_image(user_input)

                    # Display the generated image on screen
                    st.image(image, caption=f"🎨 {user_input}")
                    st.caption(f"✅ Saved to: `{filepath}`")

                    # Save image message to session
                    st.session_state.messages.append({
                        "role": "bot",
                        "content": filepath,
                        "type": "image"
                    })

                except Exception as error:
                    st.error(f"❌ Image generation failed: {error}")

    # ── Step 3: Normal Chat / Code Mode ───────
    else:
        # User wants to chat or generate code
        with st.chat_message("assistant"):
            with st.spinner("🤖 INO is thinking..."):
                try:
                    # Send message to Gemini and get response
                    response = send_message(
                        st.session_state.chat_session,
                        user_input
                    )

                    # Display the response
                    # st.markdown renders code blocks beautifully
                    st.markdown(response)

                    # Save bot response to session
                    st.session_state.messages.append({
                        "role": "bot",
                        "content": response,
                        "type": "text"
                    })

                except Exception as error:
                    st.error(f"❌ Error: {error}")


# ## 💾 Save It
# Press `Ctrl + S` and close Notepad.

# ---

# ## 🧠 What This File Does — Simple Explanation
# ```
# app.py
# ├── SIDEBAR
# │   ├── ➕ New Chat     → clears screen, fresh session
# │   ├── 💾 Save Chat   → saves to my_chats folder
# │   └── 📂 Past Chats  → click any to reload it
# │
# └── MAIN AREA
#     ├── Shows all messages in order
#     ├── 🎨 Image Mode ON  → generates image from prompt
#     └── 🎨 Image Mode OFF → chats with Gemini AI