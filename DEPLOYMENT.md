# 🚀 Deployment Guide

This guide will help you deploy LOLMeme to various platforms.

## Prerequisites

1. **Hugging Face Account**: Sign up at [huggingface.co](https://huggingface.co)
2. **GitHub Account**: For version control
3. **Hugging Face Token**: Get your API token from [Hugging Face Settings](https://huggingface.co/settings/tokens)

## Backend Deployment (Hugging Face Spaces)

### Option 1: Using Hugging Face Spaces UI

1. **Fork this repository** to your GitHub account
2. **Go to [Hugging Face Spaces](https://huggingface.co/spaces)**
3. **Click "Create new Space"**
4. **Configure your Space**:
   - **Owner**: Your username
   - **Space name**: `lolmeme-backend`
   - **License**: MIT
   - **SDK**: **Gradio** (we'll change this to Flask)
   - **Space hardware**: CPU (free tier)
5. **Click "Create Space"**
6. **Upload files**:
   - Upload `backend/app.py` as `app.py`
   - Upload `backend/requirements.txt` as `requirements.txt`
   - Create a new file called `README.md` with:
     ```markdown
     ---
     title: LOLMeme Backend
     emoji: 🤖
     colorFrom: blue
     colorTo: purple
     sdk: docker
     app_port: 5000
     ---
     ```
7. **Set environment variables**:
   - Go to Settings → Repository secrets
   - Add `HF_TOKEN` with your Hugging Face token
8. **Deploy**: The space will automatically build and deploy

### Option 2: Using Git

1. **Clone your forked repository**
2. **Create a new Space** on Hugging Face
3. **Push to the Space**:
   ```bash
   git remote add space https://huggingface.co/spaces/YOUR_USERNAME/lolmeme-backend
   git push space main
   ```

## Frontend Deployment (Vercel)

### Option 1: Using Vercel UI

1. **Go to [Vercel](https://vercel.com)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Import your GitHub repository**
5. **Configure the project**:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
6. **Add environment variables**:
   - `VITE_API_URL`: Your backend URL (e.g., `https://your-username-lolmeme-backend.hf.space`)
7. **Deploy**

### Option 2: Using Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   cd frontend
   vercel
   ```

## Frontend Deployment (Netlify)

1. **Go to [Netlify](https://netlify.com)**
2. **Sign up/Login** with GitHub
3. **Click "New site from Git"**
4. **Choose your repository**
5. **Configure build settings**:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
6. **Deploy site**

## Environment Variables

### Backend (Hugging Face Spaces)

- `HF_TOKEN`: Your Hugging Face API token (required)

### Frontend (Vercel/Netlify)

- `VITE_API_URL`: Your backend URL (e.g., `https://your-username-lolmeme-backend.hf.space`)

## Custom Domain (Optional)

### Vercel

1. **Go to your project settings**
2. **Click "Domains"**
3. **Add your custom domain**
4. **Configure DNS** as instructed

### Netlify

1. **Go to your site settings**
2. **Click "Domain management"**
3. **Add custom domain**
4. **Configure DNS** as instructed

## Monitoring and Analytics

### Backend Monitoring

- **Hugging Face Spaces**: Built-in monitoring and logs
- **Health Check**: `https://your-space.hf.space/health`

### Frontend Analytics

- **Vercel Analytics**: Built-in with Vercel
- **Google Analytics**: Add tracking code to `index.html`

## Troubleshooting

### Common Issues

1. **CORS Errors**: Make sure your backend URL is correct in frontend
2. **API Token Issues**: Verify your `HF_TOKEN` is set correctly
3. **Build Failures**: Check the build logs for dependency issues

### Support

- **GitHub Issues**: Create an issue in the repository
- **Hugging Face**: Check the Spaces documentation
- **Vercel/Netlify**: Check their respective documentation

## Performance Optimization

1. **Image Optimization**: Use WebP format for better compression
2. **Caching**: Implement proper caching headers
3. **CDN**: Use Vercel's or Netlify's CDN for faster loading

## Security

1. **Environment Variables**: Never commit sensitive data
2. **API Rate Limiting**: Implement rate limiting for production
3. **HTTPS**: Always use HTTPS in production
4. **Input Validation**: Validate all user inputs

---

**🎯 Happy Deploying!**
