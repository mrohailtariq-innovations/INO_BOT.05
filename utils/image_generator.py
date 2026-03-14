# ============================================
# image_generator.py
# This file generates images from text prompts
# using Pollinations.ai — a FREE image generation
# service that requires NO extra API key.
#
# How it works:
# 1. User types a description e.g. "a sunset over mountains"
# 2. We send that description to Pollinations.ai as a URL
# 3. Pollinations returns a generated image
# 4. We save that image inside the assets/ folder
# ============================================

import requests                    # To send requests to the image generation website
import os                          # To create folders and handle file paths
from datetime import datetime      # To create unique filenames using current time
from PIL import Image              # To open and save the image (from pillow library)
from io import BytesIO             # To convert the raw image data into a file


# Folder where all generated images will be saved
IMAGES_FOLDER = "assets"


# ─────────────────────────────────────────────
# FUNCTION 1: Generate an Image from a Prompt
# ─────────────────────────────────────────────
def generate_image(prompt):
    """
    Takes a text prompt from the user,
    sends it to Pollinations.ai,
    saves the returned image to the assets folder,
    and returns the file path + the image itself.

    prompt → a text description like "a cat on the moon"
    """

    # Create the assets folder if it doesn't exist yet
    os.makedirs(IMAGES_FOLDER, exist_ok=True)

    # ── Step 1: Build the URL ──────────────────
    # Pollinations.ai works by putting your prompt inside a URL
    # We use requests.utils.quote() to handle spaces and special characters
    # Example: "a cat on moon" becomes "a%20cat%20on%20moon"
    encoded_prompt = requests.utils.quote(prompt)

    # The full URL that will generate our image
    # width and height control the image size
    # nologo=true removes the Pollinations watermark
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=768&height=768&nologo=true"

    # ── Step 2: Send the Request ───────────────
    # We send a GET request to the URL and wait up to 60 seconds
    # This is like opening the URL in a browser — it returns image data
    print(f"🎨 Sending request to generate: {prompt}")
    response = requests.get(url, timeout=60)

    # ── Step 3: Check if it Worked ────────────
    # Status code 200 means SUCCESS
    # Any other code means something went wrong
    if response.status_code != 200:
        raise Exception(
            f"❌ Image generation failed! "
            f"Status code: {response.status_code}"
        )

    # ── Step 4: Save the Image ────────────────
    # Create a unique filename using current date and time
    # Example: image_20260308_103045.png
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}.png"
    filepath = os.path.join(IMAGES_FOLDER, filename)

    # Convert the raw response content into an actual image
    # BytesIO turns the raw bytes into something PIL can read
    image = Image.open(BytesIO(response.content))

    # Save the image to our assets folder
    image.save(filepath)
    print(f"✅ Image saved to: {filepath}")

    # Return BOTH the filepath and the image object
    # filepath → used to show where it was saved
    # image    → used to display it directly in the app
    return filepath, image




# ## 🧠 What This File Does — Simple Explanation
# This file has ONE main function that generates images from text prompts:
# User types    →  "a dragon flying over a city"
#       ↓
# We build URL  →  pollinations.ai/prompt/a%20dragon...
#       ↓
# We get image  →  raw image data comes back
#       ↓
# We save it    →  assets/image_20260308_103045.png
#       ↓
# We return it  →  filepath + image shown in app