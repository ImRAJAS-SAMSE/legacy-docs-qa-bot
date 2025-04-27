# 📄 Legacy Docs Q&A Bot

> Upload your legacy PDF/TXT business reports and instantly ask questions with AI-powered retrieval!

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?style=for-the-badge&logo=streamlit) 
![Made with R2R](https://img.shields.io/badge/Powered%20by-R2R-blueviolet?style=for-the-badge)

---

## ✨ Project Overview

**Legacy Docs Q&A Bot** allows users to upload old documents (PDFs or text files) and ask questions directly without manually searching through the files.  
It's built with [Streamlit](https://streamlit.io/) and powered by [SciPhi-AI's R2R](https://github.com/SciPhi-AI/R2R) (Retrieve-to-Read) system for fast, efficient, and intelligent document querying.

---

## ⚡ Features

- 📤 Upload legacy PDF or TXT documents
- ❓ Ask natural language questions about uploaded files
- 🧠 Get instant AI-generated answers
- 🔥 Streamlined, modern, and responsive UI
- 💬 Smart error handling and loading indicators
- 🛡️ Clean code structure ready for deployment

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/ImRAJAS-SAMSE/legacy-docs-qa.git
cd legacy-docs-qa
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the app locally:

```bash
streamlit run app.py
```

---

## 🛠️ Requirements

- Python 3.8+
- Streamlit
- r2r (SciPhi-AI client)

You can find all dependencies inside `requirements.txt`.

---

## 📂 Project Structure

```bash
legacy-docs-qa/
│
├── app.py                # Main Streamlit application
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── .gitignore             # Ignore unnecessary files
```

---

## 📚 How It Works

- Upload a `.pdf` or `.txt` file.
- The document is securely ingested into the R2R backend.
- Ask any question related to the uploaded content.
- Get AI-generated, context-aware answers in real-time.

---

## 🙌 Credits

- [SciPhi-AI's R2R](https://github.com/SciPhi-AI/R2R)
- [Streamlit](https://streamlit.io/)

---


# 💬 Contact

If you have any questions, feel free to connect with me!  
**[LinkedIn](https://www.linkedin.com/in/rajas-samse-a09b4724a/)** 

---

**Built with ❤️ to modernize legacy systems!**
