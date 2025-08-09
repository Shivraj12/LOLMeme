import { useState, useRef } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [selectedFile, setSelectedFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [memes, setMemes] = useState([])
  const [error, setError] = useState(null)
  const fileInputRef = useRef(null)

  // Random funny taglines
  const taglines = [
    "From Boring to LOL in 3 Seconds! 🤖",
    "AI + Memes = Chaos 😂",
    "Your photo called… it wants to be famous 📸",
    "Turning pixels into punchlines 🎯",
    "When AI gets creative with your pics 🎨",
    "Meme magic at your fingertips ✨",
    "Upload. Laugh. Repeat. 🔄",
    "AI-powered comedy gold 🏆"
  ]

  const [currentTagline] = useState(() => taglines[Math.floor(Math.random() * taglines.length)])

  const handleFileSelect = (event) => {
    const file = event.target.files[0]
    if (file) {
      setSelectedFile(file)
      setError(null)
      
      // Create preview
      const reader = new FileReader()
      reader.onload = (e) => {
        setPreview(e.target.result)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleDrop = (event) => {
    event.preventDefault()
    const file = event.dataTransfer.files[0]
    if (file && file.type.startsWith('image/')) {
      setSelectedFile(file)
      setError(null)
      
      const reader = new FileReader()
      reader.onload = (e) => {
        setPreview(e.target.result)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleDragOver = (event) => {
    event.preventDefault()
  }

  const generateMemes = async () => {
    if (!selectedFile) {
      setError('Please select an image first!')
      return
    }

    setLoading(true)
    setError(null)
    setMemes([])

    const formData = new FormData()
    formData.append('image', selectedFile)

    try {
      const response = await axios.post('/api/generate-memes', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })

      if (response.data.success) {
        setMemes(response.data.memes.map((memeUrl, index) => ({
          url: `/api${memeUrl}`,
          caption: response.data.captions[index] || 'Funny caption here!'
        })))
      } else {
        setError('Failed to generate memes. Please try again!')
      }
    } catch (error) {
      console.error('Error generating memes:', error)
      setError('Error generating memes. Please check your connection and try again!')
    } finally {
      setLoading(false)
    }
  }

  const downloadMeme = async (memeUrl, caption) => {
    try {
      const response = await fetch(memeUrl)
      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `lolmeme-${caption.replace(/[^a-zA-Z0-9]/g, '-')}.jpg`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (error) {
      console.error('Error downloading meme:', error)
    }
  }

  const shareOnTwitter = (memeUrl, caption) => {
    const text = `Check out this AI-generated meme: "${caption}" Created with LOLMeme! 🤖`
    const url = encodeURIComponent(window.location.href)
    const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${url}`
    window.open(twitterUrl, '_blank')
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-400 via-pink-500 to-purple-600 animate-gradient">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="meme-title text-6xl md:text-8xl text-white mb-4">
            LOLMeme 🤖
          </h1>
          <p className="text-xl md:text-2xl text-white font-bold mb-2">
            {currentTagline}
          </p>
          <p className="text-lg text-white opacity-90">
            Upload a photo → AI writes captions → You get instant memes
          </p>
        </div>

        {/* Upload Section */}
        <div className="max-w-2xl mx-auto mb-8">
          <div
            className="upload-area rounded-lg p-8 text-center cursor-pointer"
            onClick={() => fileInputRef.current?.click()}
            onDrop={handleDrop}
            onDragOver={handleDragOver}
          >
            {preview ? (
              <div className="space-y-4">
                <img
                  src={preview}
                  alt="Preview"
                  className="max-w-full h-64 object-contain mx-auto rounded-lg border-2 border-gray-300"
                />
                <p className="text-lg font-semibold text-gray-700">
                  {selectedFile?.name}
                </p>
                <button
                  onClick={(e) => {
                    e.stopPropagation()
                    setSelectedFile(null)
                    setPreview(null)
                  }}
                  className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors"
                >
                  Remove Image
                </button>
              </div>
            ) : (
              <div className="space-y-4">
                <div className="text-6xl">📸</div>
                <p className="text-xl font-semibold text-gray-700">
                  Drop your image here or click to select
                </p>
                <p className="text-gray-500">
                  Supports JPG, PNG, GIF (max 10MB)
                </p>
              </div>
            )}
          </div>

          <input
            ref={fileInputRef}
            type="file"
            accept="image/*"
            onChange={handleFileSelect}
            className="hidden"
          />

          {selectedFile && (
            <div className="text-center mt-4">
              <button
                onClick={generateMemes}
                disabled={loading}
                className="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-8 py-3 rounded-lg font-bold text-lg hover:from-purple-600 hover:to-pink-600 transition-all transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? (
                  <div className="flex items-center justify-center space-x-2">
                    <div className="loading-spinner"></div>
                    <span>Generating Memes...</span>
                  </div>
                ) : (
                  'Generate Memes! 🎯'
                )}
              </button>
            </div>
          )}

          {error && (
            <div className="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
              {error}
            </div>
          )}
        </div>

        {/* Memes Grid */}
        {memes.length > 0 && (
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-bold text-white text-center mb-8 meme-title">
              Your Generated Memes! 🎉
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {memes.map((meme, index) => (
                <div key={index} className="meme-card rounded-lg p-4">
                  <img
                    src={meme.url}
                    alt={`Meme ${index + 1}`}
                    className="w-full h-64 object-cover rounded-lg mb-4"
                  />
                  <p className="text-center font-semibold text-gray-800 mb-4">
                    "{meme.caption}"
                  </p>
                  <div className="flex space-x-2">
                    <button
                      onClick={() => downloadMeme(meme.url, meme.caption)}
                      className="flex-1 bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors"
                    >
                      📥 Download
                    </button>
                    <button
                      onClick={() => shareOnTwitter(meme.url, meme.caption)}
                      className="flex-1 bg-blue-400 text-white py-2 px-4 rounded-lg hover:bg-blue-500 transition-colors"
                    >
                      🐦 Share
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
