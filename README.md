# INO BOT.05 - Your Ultimate AI Assistant 🤖

![INO Bot Cover](https://img.shields.io/badge/AI-INO_BOT.05-blue?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit) ![Gemini](https://img.shields.io/badge/Google_Gemini-API-orange?style=for-the-badge) 

**INO BOT.05** is a highly capable, dual-interface (Web & Terminal) Artificial Intelligence assistant. Powered by **Google's Gemini 2.0 Flash** model and **Pollinations.ai**, this project offers seamless conversational AI, code generation, and text-to-image capabilities all within a single, unified experience.

Whether you prefer a sleek web interface or a fast terminal CLI, INO BOT.05 provides state-of-the-art AI tooling for developers, creators, and everyday users.

---

## 🌟 Key Features

*   💬 **Advanced Conversational AI**: Chat intelligently with the Gemini 2.0 Flash model.
*   👨‍💻 **Code Generation**: Ask INO to write, explain, or debug code in any programming language.
*   🎨 **Free Image Generation**: Instantly generate stunning images from text prompts using Pollinations.ai (No extra API key needed).
*   💾 **Persistent Chat History**: Save your valuable conversations locally as JSON files and load them anytime.
*   🌐 **Dual Interface**:
    *   **Web UI (`app.py`)**: A beautiful, interactive web application built with Streamlit.
    *   **Terminal UI (`chatbot.py`)**: A blazing-fast command-line interface for terminal power users.

---

## 🛠️ Tools & Technologies Used

*   **Language:** Python 3
*   **Web Framework:** [Streamlit](https://streamlit.io/) (for the Web UI)
*   **AI Engine:** [Google Generative AI (Gemini)](https://deepmind.google/technologies/gemini/)
*   **Image Generation:** [Pollinations.ai](https://pollinations.ai/)
*   **Environment Management:** `python-dotenv`

---

## 📂 Project Hierarchy

Understanding the structure of INO BOT.05:

```text
INO-BOT.05/
│
├── app.py                     # The Main Web UI application (Streamlit)
├── chatbot.py                 # The Terminal CLI version of the chatbot
├── .env                       # Environment variables (Store your Gemini API Key here)
├── .gitignore                 # Specifies intentionally untracked files to ignore
├── README.md                  # This documentation file
│
├── assets/                    # Directory where generated images are automatically saved
│
├── my_chats/                  # Directory where your conversation history (.json) is saved
│
├── utils/                     # Core utility modules (The Brain of the Bot)
│   ├── __init__.py            # Initializes the utils module
│   ├── chat_handler.py        # Connects to Gemini API and manages conversations
│   ├── image_generator.py     # Connects to Pollinations.ai to generate and save images
│   └── storage.py             # Handles saving, loading, and deleting chat histories locally
│
└── venv/                      # Python Virtual Environment
```

---

## 🚀 How It Works (System Functionality)

The core logic of INO BOT.05 is beautifully separated into utility modules to ensure clean, maintainable, and efficient code:

1.  **Chat Handling (`utils/chat_handler.py`)**: This module acts as the brain. It securely loads your `GEMINI_API_KEY` from the `.env` file, initializes the connection with Google's generative models, and manages the chat session state (remembering conversation history).
2.  **Image Generation (`utils/image_generator.py`)**: When an image is requested, this module parses the user's text prompt, formats it into a URL request to Pollinations.ai, retrieves the raw image data, and saves it directly into the `assets/` folder.
3.  **Storage System (`utils/storage.py`)**: Chats can be saved persistently. This module converts the chat history into a human-readable JSON format, saving it to the `my_chats/` folder. It also includes functions to list past chats, load specific sessions, and delete old ones.
4.  **User Interfaces**:
    *   **`app.py`**: Uses Streamlit's reactive session state to build a dynamic sidebar for chat history, a main chat window, and a toggle for image generation mode.
    *   **`chatbot.py`**: Uses a continuous `while` loop to listen for standard terminal inputs and commands (like `/image`, `/save`, `/clear`).

---

## ⚙️ Getting Started

### 1. Requirements and Setup
Clone the repository and set up your virtual environment:
```bash
git clone https://github.com/mrohailtariq-innovations/INO_BOT.05.git
cd INO_BOT.05
```

### 2. Configuration
Create a `.env` file in the root directory and add your Google Gemini API Key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 3. Running the Bot
**For the Web Interface:**
```bash
streamlit run app.py
```

**For the Terminal Interface:**
```bash
python chatbot.py
```

---

*Built with ❤️ utilizing the power of Gemini API.*
