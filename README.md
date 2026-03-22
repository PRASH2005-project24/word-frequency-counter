# 📊 Word Frequency Counter

A sleek, modern web app that counts word frequencies in text files. Upload a `.txt` file, search for any word, and instantly see how many times it appears — along with a visual chart of the top 15 most frequent words.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## 🌐 Live Demo

🔗 **[Try it online](https://word-frequency-counter-by-project24.streamlit.app)**


## 📸 Screenshots

### Landing Page
<p align="center">
  <img src="screenshots/landing_page.png" alt="Landing Page" width="500"/>
</p>

### Results — Word Count & Top Words Chart
<p align="center">
  <img src="screenshots/results_page.png" alt="Results Page" width="500"/>
</p>

### Mobile Responsive
<p align="center">
  <img src="screenshots/mobile_view.png" alt="Mobile View" width="300"/>
</p>

## ✨ Features

- 📁 **Drag & Drop** file upload (`.txt` files)
- 🔍 **Word Search** — case-insensitive, punctuation-stripped
- 📈 **Instant Stats** — total words, unique words, search hits
- 📊 **Top 15 Bar Chart** — visual frequency breakdown
- 🌙 **Premium Dark Theme** — glassmorphism-inspired design
- 📱 **Responsive** — works on desktop & mobile

## 🚀 Quick Start

### Prerequisites
- Python 3.8+

### Install & Run

```bash
# Clone the repo
git clone https://github.com/PRASH2005-project24/word-frequency-counter.git
cd word-frequency-counter

# Install dependencies
pip install -r requirements.txt

# Run the app
python -m streamlit run streamlit_app.py
```

Opens at `http://localhost:8501`

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core language |
| **Streamlit** | Web framework & UI |
| **collections.Counter** | Word frequency analysis |
| **re** | Text cleaning & normalization |

## 📖 How It Works

1. **Upload** a `.txt` file via drag & drop or file browser
2. **Enter** a word you want to search for
3. **Click "Count"** to analyze
4. **View results**: word count, unique words, search hits, and a top-words bar chart

## 🌐 Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file path to `streamlit_app.py`
5. Click **Deploy** 🚀

## 📁 Project Structure
```
word-frequency-counter/
├── streamlit_app.py        # Main Streamlit app
├── requirements.txt        # Dependencies
├── .streamlit/config.toml  # Dark theme config
├── screenshots/            # App screenshots
│   ├── landing_page.png
│   ├── results_page.png
│   └── mobile_view.png
├── .gitignore
└── README.md
```

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ by <a href="https://github.com/PRASH2005-project24">Prashik Chandrasheel</a></p>
