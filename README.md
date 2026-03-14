# INO BOT.05: AI Chatbot & Image Generator

![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg) ![Gemini API](https://img.shields.io/badge/Google-Gemini_API-orange.svg) 

**INO BOT.05** is a local dual-interface AI assistant built with Python. Powered by **Google Gemini 2.0 Flash** and **Pollinations.ai**, it provides intelligent chat, code generation, and text-to-image creation.

## ✨ Features
- **Conversational AI**: Chat capabilities using the Google Gemini API.
- **Text-to-Image**: Free image generation via Pollinations.ai (auto-saved locally).
- **Persistent Storage**: Save, load, and manage chat histories in JSON format.
- **Dual Interfaces**: 
  - `app.py`: Interactive Web UI built with Streamlit.
  - `chatbot.py`: Fast Terminal CLI for developers.

## 📂 Repository Structure
- `app.py` - Main Streamlit Web Application
- `chatbot.py` - Terminal Chatbot CLI
- `utils/` - Core logic (`chat_handler.py`, `image_generator.py`, `storage.py`)
- `assets/` - Directory for generated images  
- `my_chats/` - Directory for saved chat JSON logs

## 🚀 Quick Start

**1. Clone the repository**
```bash
git clone https://github.com/mrohailtariq-innovations/INO_BOT.05.git
cd INO_BOT.05
```

**2. Add your API Key**
Create a `.env` file in the root folder and add your key:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

**3. Run the Bot**
*Web UI (Streamlit):*
```bash
streamlit run app.py
```
*Terminal CLI:*
```bash
python chatbot.py
```
