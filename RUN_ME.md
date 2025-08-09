# 🚀 How to Run LOLMeme

## ✅ Prerequisites Completed
- ✅ Python virtual environment created
- ✅ Backend dependencies installed
- ✅ Frontend dependencies installed

## 🎯 Next Steps

### Step 1: Get Your Hugging Face Token
1. Go to [Hugging Face](https://huggingface.co) and sign up/login
2. Click your profile → Settings
3. Go to "Access Tokens" → "New token"
4. Select "Read" permissions
5. Copy the token (you'll need it in Step 3)

### Step 2: Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:HF_TOKEN="your_huggingface_token_here"
```

**Windows (Command Prompt):**
```cmd
set HF_TOKEN=your_huggingface_token_here
```

**macOS/Linux:**
```bash
export HF_TOKEN=your_huggingface_token_here
```

### Step 3: Start the Backend

**Open a new terminal/command prompt and run:**
```bash
# Navigate to project directory
cd "F:\CrestCorporation\Github Repos August 25\LOLMeme2\LOLMeme"

# Activate virtual environment
venv\Scripts\activate

# Start backend
cd backend
python app.py
```

**You should see:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Step 4: Start the Frontend

**Open another terminal/command prompt and run:**
```bash
# Navigate to project directory
cd "F:\CrestCorporation\Github Repos August 25\LOLMeme2\LOLMeme"

# Start frontend
cd frontend
npm run dev
```

**You should see:**
```
  VITE v5.0.8  ready in 1234 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

### Step 5: Use the App

1. **Open your browser** and go to: `http://localhost:3000`
2. **Upload an image** by dragging and dropping or clicking to select
3. **Click "Generate Memes! 🎯"**
4. **Wait 10-30 seconds** for AI processing
5. **Download or share** your generated memes!

## 🎨 Features You'll See

- 🎯 **AI-Powered Meme Generation**: Uses BLIP + LLaMA models
- 🖼️ **Drag & Drop Upload**: Easy image upload with preview
- 🎪 **5 Memes Per Image**: Multiple caption options
- 📥 **One-Click Download**: Save memes instantly
- 🐦 **Social Sharing**: Share on Twitter
- 🎨 **Viral Design**: Bright colors, playful fonts

## 🐛 Troubleshooting

### "HF_TOKEN not set"
- Make sure you've set the environment variable correctly
- Get your token from [Hugging Face Settings](https://huggingface.co/settings/tokens)

### "Module not found"
- Make sure you're in the virtual environment: `venv\Scripts\activate`
- Reinstall dependencies: `pip install -r requirements.txt`

### CORS errors
- Make sure backend is running on port 5000
- Make sure frontend is running on port 3000

### Frontend not loading
- Make sure you ran `npm run dev` in the frontend directory
- Check if port 3000 is available

## 🎯 Quick Commands Summary

```bash
# Terminal 1 - Backend
cd "F:\CrestCorporation\Github Repos August 25\LOLMeme2\LOLMeme"
venv\Scripts\activate
cd backend
python app.py

# Terminal 2 - Frontend  
cd "F:\CrestCorporation\Github Repos August 25\LOLMeme2\LOLMeme"
cd frontend
npm run dev
```

## 🎉 You're Ready!

Once both servers are running:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

**🤖 Happy meme generating!**
