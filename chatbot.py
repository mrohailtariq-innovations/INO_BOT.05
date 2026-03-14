# ============================================
# chatbot.py
# This is the TERMINAL version of INO chatbot.
# Run this file to chat directly in the command
# line without any web interface.
#
# How to run:
#   python chatbot.py
#
# Available commands while chatting:
#   /image <prompt>  → Generate an image
#   /save            → Save the current chat
#   /clear           → Start a brand new chat
#   /quit            → Exit the chatbot
# ============================================

# Import our utility functions from the utils folder
from utils.chat_handler import init_model, start_chat, send_message, get_history
from utils.storage import save_chat
from utils.image_generator import generate_image


# ─────────────────────────────────────────────
# FUNCTION: Print the Welcome Banner
# ─────────────────────────────────────────────
def print_banner():
    """
    Prints a welcome message when the chatbot starts.
    Just for a nice user experience.
    """
    print("\n")
    print("=" * 55)
    print("        🤖 Welcome to INO - Your AI Assistant")
    print("=" * 55)
    print("  💬 Chat    → Just type your message")
    print("  👨‍💻 Code    → Ask me to write any code")
    print("  🎨 Image   → /image a sunset over mountains")
    print("  💾 Save    → /save")
    print("  🔄 Clear   → /clear  (start new chat)")
    print("  👋 Quit    → /quit")
    print("=" * 55)
    print()


# ─────────────────────────────────────────────
# MAIN FUNCTION: Runs the Chatbot
# ─────────────────────────────────────────────
def main():
    """
    This is the main function that runs everything.
    It:
    1. Starts the AI model
    2. Shows the welcome banner
    3. Keeps looping — waiting for user input
    4. Handles each command or chat message
    """

    # ── Step 1: Start the AI model ────────────
    # init_model() connects to Gemini using our API key
    print("\n⏳ Starting INO... please wait...")
    model = init_model()

    # ── Step 2: Start a chat session ──────────
    # start_chat() creates a session that remembers
    # the full conversation as we keep chatting
    chat_session = start_chat(model)

    # ── Step 3: Show the welcome banner ───────
    print_banner()

    # ── Step 4: Keep chatting in a loop ───────
    # This loop runs forever until the user types /quit
    while True:

        try:
            # Wait for the user to type something
            user_input = input("You: ").strip()
            # .strip() removes any extra spaces at start/end

            # If user pressed Enter without typing, just continue
            if not user_input:
                continue

            # ── COMMAND: Quit ──────────────────
            if user_input.lower() == "/quit":
                print("\n🤖 INO: Goodbye! Have a great day! 👋\n")
                break   # Exit the while loop and end the program

            # ── COMMAND: Save Chat ─────────────
            elif user_input.lower() == "/save":
                # Get the conversation history formatted for saving
                history = get_history(chat_session)

                if not history:
                    # Nothing to save if no messages yet
                    print("\n🤖 INO: There is nothing to save yet! Start chatting first.\n")
                else:
                    # Save the chat and show where it was saved
                    filepath = save_chat(history)
                    print(f"\n✅ Chat saved successfully to: {filepath}\n")

            # ── COMMAND: Clear / New Chat ──────
            elif user_input.lower() == "/clear":
                # Start a completely fresh chat session
                chat_session = start_chat(model)
                print("\n🔄 New chat started! Previous conversation cleared.\n")

            # ── COMMAND: Generate Image ────────
            elif user_input.lower().startswith("/image"):
                # Extract the prompt after "/image "
                # Example: "/image a cat on moon" → "a cat on moon"
                prompt = user_input[6:].strip()

                if not prompt:
                    # User typed /image but forgot to add a description
                    print("\n⚠️  Please add a description after /image")
                    print("    Example: /image a dragon flying over a city\n")
                else:
                    print("\n🎨 Generating your image, please wait...\n")
                    try:
                        # generate_image() returns the filepath and image object
                        filepath, image = generate_image(prompt)
                        print(f"✅ Image generated and saved to: {filepath}")
                        print("📁 Open the assets folder to view your image!\n")
                    except Exception as error:
                        # If image generation fails, show the error clearly
                        print(f"❌ Image generation failed: {error}\n")

            # ── NORMAL CHAT MESSAGE ────────────
            else:
                # This runs for any normal message (not a command)
                print("\n🤖 INO: thinking...\n")

                try:
                    # Send the message to Gemini and get the reply
                    response = send_message(chat_session, user_input)

                    # Print the AI's response
                    print(f"🤖 INO: {response}\n")

                except Exception as error:
                    # If something goes wrong with the API call
                    print(f"❌ Error getting response: {error}\n")

        # If user presses Ctrl+C, exit gracefully
        except KeyboardInterrupt:
            print("\n\n👋 INO: Goodbye! See you next time!\n")
            break


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────
# This means: only run main() if we run THIS file directly
# It won't run if this file is imported by another file
if __name__ == "__main__":
    main()



# ## 🧠 What This File Does — Simple Explanation
# This file is the main program for our INO chatbot. When you run it, it connects to the Gemini AI model and lets you chat with it directly in your terminal. You can type messages, ask it to generate images, save your chat history, or start a new conversation. The chatbot will keep responding until you decide to quit. It's a simple way to interact with the AI without needing a web interface!
# python chatbot.py
#         ↓
# Connects to Gemini ──→ Shows welcome banner
#         ↓
# Waits for your input
#         ↓
# /image  ──→ generates image
# /save   ──→ saves chat to my_chats folder  
# /clear  ──→ fresh new chat
# /quit   ──→ exits the program
# anything else ──→ sends to Gemini, prints reply