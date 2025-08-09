# LOLMeme 🤖

> **Upload a photo → AI writes captions → You get instant memes**

[![LOLMeme Banner](https://img.shields.io/badge/LOLMeme-AI%20Powered%20Meme%20Generator-brightgreen?style=for-the-badge&logo=robot)](https://github.com/yourusername/lolmeme)

<div align="center">
  <img src="https://via.placeholder.com/800x200/ff6b6b/ffffff?text=LOLMeme+AI+Meme+Generator" alt="LOLMeme Banner" width="800"/>
</div>

## 🎯 What is LOLMeme?

LOLMeme is an AI-powered web app that transforms your boring photos into hilarious memes in seconds! Just upload an image, and our AI will:

1. **Analyze** your image using BLIP (image captioning)
2. **Generate** 5 funny, meme-worthy captions using LLaMA-3.1-8B-Instruct
3. **Overlay** the captions on your image with classic meme styling
4. **Deliver** instant, shareable memes!

## ✨ Features

- 🎨 **AI-Powered Captions**: Uses state-of-the-art AI models for hilarious results
- 🖼️ **Drag & Drop Upload**: Easy image upload with preview
- 🎯 **5 Memes Per Image**: Get multiple caption options every time
- 📥 **One-Click Download**: Save your memes instantly
- 🐦 **Social Sharing**: Share directly to Twitter
- 🎪 **Viral Design**: Bright colors, playful fonts, meme-worthy UI
- 🚀 **Lightning Fast**: Built with React + Vite for speed

## 🎮 Live Demo

**[🚀 Try LOLMeme Now!](https://your-demo-link.com)**

*Coming soon to Hugging Face Spaces or Render!*

## 📸 Screenshots

<div align="center">
  <img src="https://via.placeholder.com/400x300/4ecdc4/ffffff?text=Upload+Interface" alt="Upload Interface" width="400"/>
  <img src="https://via.placeholder.com/400x300/45b7d1/ffffff?text=Generated+Memes" alt="Generated Memes" width="400"/>
</div>

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Core language
- **Flask** - Web framework
- **Pillow** - Image processing
- **Requests** - HTTP client
- **Hugging Face API** - AI models

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **Axios** - HTTP client

### AI Models
- **BLIP** - Image captioning
- **LLaMA-3.1-8B-Instruct** - Text generation

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Hugging Face API token

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lolmeme.git
   cd lolmeme
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   # Create .env file
   echo "HF_TOKEN=your_huggingface_token_here" > .env
   ```

5. **Run the backend**
   ```bash
   python app.py
   ```

### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Run the frontend**
   ```bash
   npm run dev
   ```

3. **Open in browser**
   ```
   http://localhost:3000
   ```

## 🎨 Usage

1. **Upload Image**: Drag & drop or click to select an image
2. **Generate Memes**: Click "Generate Memes! 🎯" button
3. **Wait for AI**: Watch the loading animation (usually 10-30 seconds)
4. **Download & Share**: Download your memes or share on Twitter!

## 🔧 Configuration

### Environment Variables

- `HF_TOKEN`: Your Hugging Face API token (required)

### Customization

- **Fonts**: Edit `frontend/src/index.css` for custom fonts
- **Colors**: Modify `frontend/tailwind.config.js` for theme colors
- **AI Models**: Update model names in `backend/app.py`

## 🚀 Deployment

### Backend (Hugging Face Spaces)

1. **Fork this repository**
2. **Create new Space** on Hugging Face
3. **Select Flask template**
4. **Set environment variables**:
   - `HF_TOKEN`: Your Hugging Face token
5. **Deploy!**

### Frontend (Vercel/Netlify)

1. **Build the project**:
   ```bash
   cd frontend
   npm run build
   ```
2. **Deploy `dist` folder** to your preferred platform

## 🤝 Contributing

We love contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** for providing amazing AI models
- **React** and **Vite** for the awesome development experience
- **TailwindCSS** for the beautiful styling framework
- **All the meme creators** who inspired this project!

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/lolmeme&type=Date)](https://star-history.com/#yourusername/lolmeme&Date)

---

<div align="center">
  <p><strong>⭐ If LOLMeme made you laugh, give it a star!</strong></p>
  <p>Made with ❤️ and 🤖 by the LOLMeme team</p>
</div>
