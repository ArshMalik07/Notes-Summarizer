
# 🧠 Smart Notes Summarizer

This is a simple Streamlit web app that summarizes long text or notes using a pre-trained Hugging Face transformer model (`facebook/bart-large-cnn`). It can take input from both text box and uploaded `.txt` files, and returns a concise summary.

---

## 🚀 Features

- Summarize any text content using a transformer-based model
- Upload `.txt` files to summarize content from documents
- Automatically adjust summary length based on input size
- Simple and clean UI built with Streamlit

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```txt
streamlit
transformers
torch
sentencepiece
```

---

## 💻 How to Run This Application

1. **Clone or download** the repository.

```bash
git clone https://github.com/your-username/notes-summarizer.git
cd notes-summarizer
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On macOS/Linux
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app:**
```bash
streamlit run summarizer.py
or
python -m streamlit run summarizer.py
```

5. **Open your browser:**

Streamlit will automatically open the app in your browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
.
├── summarizer.py        # Main application file
├── requirements.txt     # List of required packages
└── README.md            # Project documentation
```

---

## 🧠 Model Used

- Model: [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)
- Task: Summarization
- Framework: Hugging Face Transformers

---


## 🙋 Author

Made with ❤️ by Arsh Malek
