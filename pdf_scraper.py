import streamlit as st
from PyPDF2 import PdfReader

# Streamlit UI
st.title("PDF Text Extractor")

# 1. Import Button
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("File uploaded successfully.")
    st.write("Extracting text...")

    # 2. Extract Text from PDF
    try:
        pdf_reader = PdfReader(uploaded_file)
        text = []

        for page in pdf_reader.pages:
            page_text = page.extract_text()
            text.append(page_text)

        # 3. Display Extracted Text as Tables
        st.subheader("Extracted Text:")
        
        for i, page_text in enumerate(text, start=1):
            st.subheader(f"Page {i}:")
            lines = page_text.split("\n")
            table_data = [line.split() for line in lines if line.strip() != ""]
            st.table(table_data)

    except Exception as e:
        st.error(f"An error occurred while processing the PDF: {str(e)}")
else:
    st.info("Upload a PDF file to start the extraction.")
