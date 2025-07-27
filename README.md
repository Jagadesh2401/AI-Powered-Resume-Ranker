# 🧠 AI-Powered Resume Ranker

A web application that uses Natural Language Processing (NLP) to rank PDF resumes against a job description using similarity scores.

---

## 🚀 Features

- 📝 Upload multiple resumes (PDF)
- 📄 Paste job description
- ⚙️ NLP-based text preprocessing (SpaCy)
- 🧮 TF-IDF vectorization and cosine similarity scoring
- 📊 Rank candidates based on job fit
- 🌐 Simple web UI using Flask

---

## 🧰 Tech Stack

- Python
- Flask
- SpaCy (for text preprocessing)
- Scikit-learn (TF-IDF and similarity scoring)
- PyMuPDF (for PDF text extraction)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/AI-Powered-Resume-Ranker.git
cd AI-Powered-Resume-Ranker

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download SpaCy model
python -m spacy download en_core_web_sm

# Run the app
python app.py
