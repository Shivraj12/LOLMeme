# 🚀 Quick Start Guide

## Prerequisites

- Python 3.8+
- Node.js 16+
- Hugging Face API token

## 🎯 One-Command Setup

### Windows
```bash
setup.bat
```

### macOS/Linux
```bash
chmod +x setup.sh
./setup.sh
```

## 🔧 Manual Setup

### 1. Backend Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt
cd ..

# Set environment variable
# Windows:
set HF_TOKEN=your_huggingface_token_here
# macOS/Linux:
export HF_TOKEN=your_huggingface_token_here

# Start backend
cd backend
python app.py
```

### 2. Frontend Setup

```bash
# Install dependencies
cd frontend
npm install

# Start frontend
npm run dev
```

### 3. Access the App

- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

## 🎨 Features

- ✅ **AI-Powered Meme Generation**: Uses BLIP + LLaMA models
- ✅ **Drag & Drop Upload**: Easy image upload with preview
- ✅ **5 Memes Per Image**: Multiple caption options
- ✅ **One-Click Download**: Save memes instantly
- ✅ **Social Sharing**: Share on Twitter
- ✅ **Viral Design**: Bright colors, playful fonts
- ✅ **Responsive**: Works on mobile and desktop

## 🔍 Testing

1. **Upload an image** (JPG, PNG, GIF)
2. **Click "Generate Memes! 🎯"**
3. **Wait 10-30 seconds** for AI processing
4. **Download or share** your memes!

## 🐛 Troubleshooting

### Common Issues

1. **"HF_TOKEN not set"**
   - Make sure you've set the environment variable
   - Get your token from [Hugging Face Settings](https://huggingface.co/settings/tokens)

2. **"Module not found"**
   - Make sure you're in the virtual environment
   - Run `pip install -r requirements.txt` again

3. **"npm command not found"**
   - Install Node.js from [nodejs.org](https://nodejs.org)

4. **CORS errors**
   - Make sure backend is running on port 5000
   - Check that frontend is using correct backend URL

### Support

- **GitHub Issues**: Create an issue in the repository
- **Documentation**: Check the main README.md
- **Deployment**: See DEPLOYMENT.md

## 🎯 Next Steps

1. **Get your Hugging Face token** from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. **Test the app** with your own images
3. **Deploy to production** using the deployment guide
4. **Share with friends** and get feedback!

---

**🤖 Happy meme generating!**
