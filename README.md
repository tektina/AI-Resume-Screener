# 🤖 AI Resume Screener

An intelligent, lightweight resume screening tool built with **Streamlit** and **scikit-learn** that automatically ranks candidate resumes against a job description using TF-IDF vectorization and cosine similarity.

---

## 🚀 Demo

Upload multiple PDF resumes, paste a job description, and instantly get a ranked list of candidates by match percentage — no manual reading required.

---

## ✨ Features

- 📄 **Bulk PDF Upload** — Screen multiple resumes in a single run
- 🧠 **AI-Powered Matching** — Uses TF-IDF + Cosine Similarity to score each resume against the job description
- 📊 **Ranked Results Table** — Candidates sorted by match percentage, highest first
- ⚡ **Instant Analysis** — Results appear in seconds, no model training required
- 🖥️ **Simple Web UI** — Clean Streamlit interface, no technical knowledge needed to use

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| PDF Parsing | PyPDF2 |
| Vectorization | scikit-learn (TF-IDF) |
| Similarity Scoring | scikit-learn (Cosine Similarity) |
| Data Display | pandas |
| Language | Python 3.8+ |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/tektina/AI-Resume-Screener.git
cd AI-Resume-Screener
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## 📋 Requirements

Create a `requirements.txt` with the following:

```
streamlit
PyPDF2
pandas
scikit-learn
```

---

## 🧑‍💻 How It Works

1. **Paste a job description** into the text area
2. **Upload one or more PDF resumes** using the file uploader
3. Click **"Screen Resumes"**
4. The app extracts text from each PDF, then:
   - Combines the job description + all resumes into a document corpus
   - Applies **TF-IDF vectorization** to convert text into numerical vectors
   - Computes **cosine similarity** between the job description vector and each resume vector
5. Results are displayed as a **ranked table** showing each candidate's match percentage

---

## 📁 Project Structure

```
AI-Resume-Screener/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📸 Screenshot

> *(Add a screenshot of the running app here)*

---

## 🔮 Future Improvements

- [ ] Export results to CSV
- [ ] Highlight matched keywords in each resume
- [ ] Support for DOCX resume uploads
- [ ] Named entity extraction (skills, education, experience)
- [ ] Threshold-based shortlisting (e.g. auto-flag candidates above 70%)
- [ ] Integration with applicant tracking systems (ATS)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**tektina**  
[GitHub Profile](https://github.com/tektina)
