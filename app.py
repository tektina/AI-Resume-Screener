import streamlit as st
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

st.title("AI Resume Screening Tool")

job_desc = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)", type="pdf", accept_multiple_files=True
)

if st.button("Screen Resumes"):
    resumes = []
    names = []

    for file in uploaded_files:
        resumes.append(extract_text(file))
        names.append(file.name)

    documents = [job_desc] + resumes

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

    result = pd.DataFrame({
        "Resume": names,
        "Match Percentage": scores * 100
    })

    result = result.sort_values(by="Match Percentage", ascending=False)

    st.dataframe(result)