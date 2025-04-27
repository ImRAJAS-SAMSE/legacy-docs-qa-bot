import streamlit as st
from r2r import R2RClient
import tempfile
import os
import time

st.set_page_config(page_title="Legacy Docs Q&A Bot", page_icon="📄", layout="centered")

client = R2RClient()

st.markdown("<h1 style='text-align: center;'>📄 Legacy Docs Q&A Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload legacy documents and interact with them using AI!</p>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Upload your document")
    uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])
    temperature = st.slider("Answer Creativity (Temperature)", 0.0, 1.0, 0.3, 0.05)
    max_tokens = st.slider("Max Answer Length (Tokens)", 50, 500, 200, 10)
    st.markdown("---")
    st.info("Adjust the settings for how the AI answers!")

if "document_id" not in st.session_state:
    st.session_state["document_id"] = None
if "file_uploaded" not in st.session_state:
    st.session_state["file_uploaded"] = False

if uploaded_file and not st.session_state["file_uploaded"]:
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    with st.spinner("🔄 Uploading and processing your document..."):
        time.sleep(1)
        response = client.documents.create(file_path=tmp_file_path)
        st.session_state["document_id"] = response.data[0].id
        st.session_state["file_uploaded"] = True
    
    st.success("✅ Document uploaded successfully! You can now ask questions below.")

if st.session_state["document_id"]:
    st.markdown("---")
    st.subheader("💬 Ask Your Questions")
    question = st.text_input("Type your question about the uploaded document:")

    if question:
        with st.spinner("🔎 Searching for the answer..."):
            time.sleep(1)
            response = client.retrieval.rag(
                query=question,
                document_ids=[st.session_state["document_id"]],
                temperature=temperature,
                max_tokens=max_tokens
            )
        
        if response and response.data.answer:
            st.success("✅ Answer found!")
            st.markdown(f"**🧠 Answer:** {response.data.answer}")
        else:
            st.error("❌ Could not find an answer. Try rephrasing your question.")

st.markdown("---")
st.caption("🚀 Powered by [R2R](https://github.com/SciPhi-AI/R2R) | Built with ❤️ using Streamlit")

custom_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 0.5em 1em;
        border-radius: 5px;
        font-size: 1em;
        font-weight: bold;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
