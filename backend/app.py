from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import requests
import json
from PIL import Image, ImageDraw, ImageFont
import io
import base64
from datetime import datetime
import uuid
import traceback
import time

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure static folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_hf_token() -> str:
    token = os.environ.get('HF_TOKEN')
    if not token:
        raise Exception("HF_TOKEN environment variable not set")
    return token

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def call_huggingface_api(model: str, inputs, task: str = "text-generation", max_retries: int = 3):
    """Call Hugging Face Inference API with basic retry and appropriate content-type.
    - task "image-to-text": inputs should be bytes (image content)
    - task "text-generation": inputs is prompt str
    """
    token = get_hf_token()

    # Base URL
    url = f"https://api-inference.huggingface.co/models/{model}"

    for attempt in range(1, max_retries + 1):
        try:
            if task == "image-to-text":
                headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                }
                response = requests.post(url, headers=headers, data=inputs, timeout=60)
            else:
                headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                }
                payload = {
                    "inputs": inputs,
                    "parameters": {
                        "max_new_tokens": 120,
                        "temperature": 0.9,
                        "top_p": 0.95,
                        "repetition_penalty": 1.05,
                    },
                    "options": {"wait_for_model": True},
                }
                response = requests.post(url, headers=headers, json=payload, timeout=60)

            if response.status_code == 200:
                return response.json()

            # If the model is loading or rate-limited, retry
            should_retry = response.status_code in (429, 503)
            # HF sometimes returns a JSON error message
            try:
                err_json = response.json()
            except Exception:
                err_json = None

            print(f"HF API error (attempt {attempt}/{max_retries}) status={response.status_code} text={response.text[:300]} err_json={err_json}")

            if should_retry and attempt < max_retries:
                time.sleep(2 * attempt)
                continue

            # No retry left or not retryable
            raise Exception(f"HF API call failed ({response.status_code}): {response.text}")

        except Exception as e:
            print(f"Error calling HF API (attempt {attempt}/{max_retries}): {e}")
            if attempt >= max_retries:
                raise
            time.sleep(2 * attempt)


def generate_funny_captions(image_description: str):
    """Generate funny captions using LLaMA 3.1 8B Instruct"""
    prompt = f"""You are a meme writer.
Based on this image description: "{image_description}"
Generate exactly 5 short, meme-worthy captions.
Rules:
- Keep each under 60 characters
- Vary styles: sarcastic, absurd, relatable, dramatic, punny
- No numbering, return one caption per line only
"""

    try:
        response = call_huggingface_api(
            "meta-llama/Llama-3.1-8B-Instruct",
            prompt,
            "text-generation",
        )

        # Parse the response to extract captions
        text = ""
        if isinstance(response, list) and len(response) > 0:
            # Standard text-generation response shape
            text = response[0].get('generated_text', '')
        elif isinstance(response, dict) and 'generated_text' in response:
            text = response.get('generated_text', '')
        else:
            text = str(response)

        lines = [ln.strip() for ln in text.split('\n')]
        captions = []
        for ln in lines:
            if not ln:
                continue
            # Strip potential numbering
            ln = ln.lstrip("-•*0123456789. )(")
            if 2 <= len(ln) <= 90:
                captions.append(ln)
            if len(captions) == 5:
                break

        # Fallbacks if not enough
        while len(captions) < 5:
            captions.append("AI couldn't think of anything funnier than this")

        return captions[:5]

    except Exception as e:
        print(f"Error generating captions: {e}")
        return [
            "When AI tries to be funny",
            "This is what happens",
            "Plot twist: It's actually good",
            "Nobody expects the AI caption",
            "This meme writes itself",
        ]


def overlay_text_on_image(image_path, text, output_path):
    """Overlay text on image using Pillow"""
    try:
        with Image.open(image_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')

            draw_img = img.copy()
            draw = ImageDraw.Draw(draw_img)

            try:
                font_size = max(24, min(img.width, img.height) // 12)
                font = ImageFont.truetype("arial.ttf", font_size)
            except Exception:
                font = ImageFont.load_default()

            # Calculate text position (center bottom)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (img.width - text_width) // 2
            y = max(10, img.height - text_height - 24)

            # Outline
            outline_color = "black"
            outline_width = max(2, font.size // 18)
            for dx in range(-outline_width, outline_width + 1):
                for dy in range(-outline_width, outline_width + 1):
                    if dx == 0 and dy == 0:
                        continue
                    draw.text((x + dx, y + dy), text, font=font, fill=outline_color)

            # Fill
            draw.text((x, y), text, font=font, fill="white")

            draw_img.save(output_path, "JPEG", quality=95)

    except Exception as e:
        print(f"Error overlaying text: {e}")
        with Image.open(image_path) as img:
            img.convert('RGB').save(output_path, "JPEG", quality=90)


@app.route('/health', methods=['GET'])
def health_check():
    try:
        token_set = bool(os.environ.get('HF_TOKEN'))
        return jsonify({"status": "OK", "message": "LOLMeme API is running!", "hf_token_set": token_set})
    except Exception as e:
        return jsonify({"status": "ERROR", "error": str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check_api_prefixed():
    # Allow health check via the same /api prefix used by the dev proxy
    return health_check()

@app.route('/ping', methods=['GET'])
def ping():
    return "pong"


@app.route('/api/generate-memes', methods=['POST'])
def generate_memes():
    """Generate memes from uploaded image"""
    try:
        print("Received meme generation request")

        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No image selected"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type"}), 400

        # Save original image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        original_filename = f"original_{timestamp}_{unique_id}.jpg"
        original_path = os.path.join(UPLOAD_FOLDER, original_filename)
        file.save(original_path)
        print(f"Saved original image: {original_path}")

        # BLIP: image description
        image_description = "An image"
        try:
            print("Calling BLIP for image caption...")
            with open(original_path, "rb") as f:
                image_bytes = f.read()
            blip_response = call_huggingface_api(
                "Salesforce/blip-image-captioning-base",
                image_bytes,
                "image-to-text",
            )
            if isinstance(blip_response, list) and blip_response:
                image_description = blip_response[0].get('generated_text', image_description)
            elif isinstance(blip_response, dict):
                image_description = blip_response.get('generated_text', image_description)
            print(f"BLIP description: {image_description}")
        except Exception as e:
            print(f"BLIP failed, using generic description. Error: {e}")

        # LLaMA: funny captions
        print("Calling LLaMA for funny captions...")
        captions = generate_funny_captions(image_description)
        print(f"Generated captions: {captions}")

        # Create memes
        meme_urls = []
        for i, caption in enumerate(captions):
            meme_filename = f"meme_{timestamp}_{unique_id}_{i+1}.jpg"
            meme_path = os.path.join(UPLOAD_FOLDER, meme_filename)
            overlay_text_on_image(original_path, caption, meme_path)
            meme_urls.append(f"/static/{meme_filename}")

        return jsonify({
            "success": True,
            "memes": meme_urls,
            "captions": captions,
            "description": image_description,
        })

    except Exception as e:
        print(f"Error generating memes: {e}")
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500


@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    print("Starting LOLMeme backend...")
    print(f"HF_TOKEN set: {bool(os.environ.get('HF_TOKEN'))}")
    print(f"Upload folder: {UPLOAD_FOLDER}")
    app.run(debug=True, host='0.0.0.0', port=5000)
