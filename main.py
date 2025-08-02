import streamlit as st
from transformers import pipeline, AutoTokenizer

st.set_page_config(page_title="Notes Summarizer", layout="centered")

# Load summarization model and tokenizer
MODEL_NAME = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=MODEL_NAME, framework="pt")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Title and instructions
st.title("🧠 Smart Notes Summarizer")
st.markdown("Paste your notes or upload a `.txt` file to get a summary.")

# File uploader
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

# Text input (fallback if no file)
input_text = ""
if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")
else:
    input_text = st.text_area("Or, type your text here:", height=300)

# Function to split long input into chunks (approx. 1024 tokens per chunk)
def split_text_into_chunks(text, max_tokens=1024):
    words = text.split()
    chunks = []
    current_chunk = []

    token_count = 0
    for word in words:
        token_len = len(tokenizer.tokenize(word))
        if token_count + token_len > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            token_count = token_len
        else:
            current_chunk.append(word)
            token_count += token_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# Summarize button
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("Summarizing..."):

            # Split text into manageable chunks
            chunks = split_text_into_chunks(input_text)

            # Set summary length based on input size
            summaries = []
            for chunk in chunks:
                word_count = len(chunk.split())
                if word_count < 150:
                    min_len, max_len = 30, 60
                elif word_count < 300:
                    min_len, max_len = 40, 100
                else:
                    min_len, max_len = 60, 150

                try:
                    summary = summarizer(
                        chunk,
                        max_length=max_len,
                        min_length=min_len,
                        do_sample=False
                    )
                    summaries.append(summary[0]['summary_text'])
                except Exception as e:
                    summaries.append(f"[Error while summarizing a chunk: {str(e)}]")

            # Final summary
            final_summary = "\n\n".join(summaries)
            st.subheader("📄 Summary:")
            st.success(final_summary)

    else:
        st.warning("Please provide some input text or upload a file.")
