# 📷 Prompt2Pixel – AI Image Generator

**Turn your imagination into pixels with AI!**

Prompt2Pixel is an AI-powered text-to-image generator built using Python and Pollinations.ai. It transforms user-provided text prompts into creative AI-generated images and automatically downloads and saves them in PNG format.

## 🚀 Features

- Generate AI images from text prompts.
- Simple and interactive command-line interface.
- Automatic image downloading.
- Save generated images in PNG format.
- Automatically create an output directory.
- Timestamp-based image filenames.
- Error handling for failed requests.
- Custom image dimensions (1024 × 1024).

## 🛠️ Technologies Used

- Python 3
- Pollinations.ai API
- URL Encoding
- urllib
- pathlib
- datetime

## 📂 Project Structure

```text
Prompt2Pixel/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── generated_images/
    ├── image_20261124_185300.png
    └── image_20261124_190000.png
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Prompt2Pixel.git
```

### 2. Navigate to the project directory

```bash
cd Prompt2Pixel
```

### 3. Run the application

```bash
python main.py
```

No additional Python packages are required for the current implementation because it uses Python standard-library modules.

## 💻 Usage

Run the Python application:

```bash
python main.py
```

Enter your desired image prompt:

```text
=== AI Image Generator ===

Enter your image prompt:
A futuristic sports car driving through a neon city at night

Generating image... Please wait.

Image generated successfully!

Saved at: generated_images/image_20261124_185300.png
```

## 🖼️ Output

Generated images are automatically stored inside the `generated_images` directory.

Each image is saved with a unique timestamp-based filename.

## 🔧 Configuration

The application currently uses the Pollinations.ai image-generation endpoint.

Image dimensions can be modified in the URL:

```python
url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
```

## 🔮 Future Improvements

- [ ] Streamlit web interface.
- [ ] Image preview functionality.
- [ ] Download button.
- [ ] Prompt history.
- [ ] Multiple image generation.
- [ ] Custom image dimensions.
- [ ] Groq API integration for prompt enhancement.

## 🔐 Security

- Never upload API keys or passwords to GitHub.
- Keep `.env` files excluded using `.gitignore`.
- Follow the image provider's API terms and usage limits.

## 👨‍💻 Author

**Shaik Nawaz Shareef**

GitHub: https://github.com/ShaikNawazShareef

## ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.

---

**Prompt2Pixel – Turn your imagination into pixels!**
