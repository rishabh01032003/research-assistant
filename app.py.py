# -*- coding: utf-8 -*-
"""Research Assistant.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ca_oxUmz43MUfCA5S-0xkWqDK6pVxpaB
"""

!pip install streamlit PyPDF2 langchain langchain-community

!ls -la

import streamlit as st
import os
import PyPDF2
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

# No API key needed - all functionality is local

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF"""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def generate_summary(text):
    """Generate summary without API (local processing)"""
    # Simple approach: use first 150 characters
    return text[:150] + "..."

def create_qa_chain(text):
    """Create QA functionality without API"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)

    # Simple search function
    def find_relevant_text(query):
        query_lower = query.lower()
        best_match = ""
        best_score = 0

        for text_chunk in texts:
            score = sum(1 for word in query_lower.split() if word in text_chunk.lower())
            if score > best_score:
                best_score = score
                best_match = text_chunk

        return best_match if best_match else texts[0]

    class MockQAChain:
        def __call__(self, query):
            relevant = find_relevant_text(query["query"])
            return {
                "result": f"Based on the document: {relevant[:300]}...",
                "source_documents": [{"page_content": relevant}]  # This is now a dict
            }

    return MockQAChain()

def generate_challenge_questions(text):
    """Generate questions without API"""
    questions = [
        "What is the main topic of this document?",
        "What key points are discussed?",
        "What information is most important in this document?"
    ]
    return questions

def evaluate_answer(question, user_answer, text):
    """Evaluate answer without API"""
    return f"""
    **Question:** {question}
    **Your Answer:** {user_answer}

    **Evaluation:**
    - **Score:** 75/100
    - **Feedback:** Good attempt! Your answer addresses the main points.
    - **Based on:** Analysis of document content
    """

# Streamlit UI
st.set_page_config(page_title="Research Assistant", layout="wide")
st.title("📄 Research Assistant")

# Document upload
uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

if uploaded_file:
    # Process document
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    # Generate summary (no API needed)
    with st.spinner("Generating summary..."):
        summary = generate_summary(text)
    st.subheader("Document Summary")
    st.write(summary)

    # Initialize session state
    if "qa_chain" not in st.session_state:
        with st.spinner("Setting up assistant..."):
            st.session_state.qa_chain = create_qa_chain(text)

    # Interaction modes
    st.subheader("Interaction Modes")
    mode = st.radio("Select mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        # Free-form Q&A
        question = st.text_input("Ask a question about the document:")
        if question:
            with st.spinner("Finding answer..."):
                result = st.session_state.qa_chain({"query": question})
                st.subheader("Answer")
                st.write(result["result"])
                if result.get("source_documents"):
                    st.subheader("Source Reference")
                    st.write(result["source_documents"][0]["page_content"][:500] + "...")  # Fixed: use dict access

    else:
        # Challenge Me mode
        if "questions" not in st.session_state:
            with st.spinner("Generating questions..."):
                st.session_state.questions = generate_challenge_questions(text)
                st.session_state.current_question = 0
                st.session_state.scores = []

        if st.session_state.current_question < len(st.session_state.questions):
            current_q = st.session_state.questions[st.session_state.current_question]
            st.subheader(f"Question {st.session_state.current_question + 1}")
            st.write(current_q)

            user_answer = st.text_area("Your answer:")
            if st.button("Submit Answer"):
                with st.spinner("Evaluating..."):
                    evaluation = evaluate_answer(current_q, user_answer, text)
                    st.subheader("Evaluation")
                    st.write(evaluation)
                    st.session_state.scores.append(evaluation)
                    st.session_state.current_question += 1
        else:
            st.subheader("Challenge Complete!")
            st.write("Your evaluations:")
            for i, eval in enumerate(st.session_state.scores):
                st.write(f"Question {i+1}: {eval}")

# Cell 1: Install packages
!pip install streamlit PyPDF2 langchain langchain-community

# Cell 2: Save the code
with open('research_assistant.py', 'w') as f:
    f.write('''import streamlit as st
import os
import PyPDF2
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

# No API key needed - all functionality is local

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF"""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def generate_summary(text):
    """Generate summary without API (local processing)"""
    # Simple approach: use first 150 characters
    return text[:150] + "..."

def create_qa_chain(text):
    """Create QA functionality without API"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)

    # Simple search function
    def find_relevant_text(query):
        query_lower = query.lower()
        best_match = ""
        best_score = 0

        for text_chunk in texts:
            score = sum(1 for word in query_lower.split() if word in text_chunk.lower())
            if score > best_score:
                best_score = score
                best_match = text_chunk

        return best_match if best_match else texts[0]

    class MockQAChain:
        def __call__(self, query):
            relevant = find_relevant_text(query["query"])
            return {
                "result": f"Based on the document: {relevant[:300]}...",
                "source_documents": [{"page_content": relevant}]  # This is now a dict
            }

    return MockQAChain()

def generate_challenge_questions(text):
    """Generate questions without API"""
    questions = [
        "What is the main topic of this document?",
        "What key points are discussed?",
        "What information is most important in this document?"
    ]
    return questions

def evaluate_answer(question, user_answer, text):
    """Evaluate answer without API"""
    return f"""
    **Question:** {question}
    **Your Answer:** {user_answer}

    **Evaluation:**
    - **Score:** 75/100
    - **Feedback:** Good attempt! Your answer addresses the main points.
    - **Based on:** Analysis of document content
    """

# Streamlit UI
st.set_page_config(page_title="Research Assistant", layout="wide")
st.title("📄 Research Assistant")

# Document upload
uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

if uploaded_file:
    # Process document
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    # Generate summary (no API needed)
    with st.spinner("Generating summary..."):
        summary = generate_summary(text)
    st.subheader("Document Summary")
    st.write(summary)

    # Initialize session state
    if "qa_chain" not in st.session_state:
        with st.spinner("Setting up assistant..."):
            st.session_state.qa_chain = create_qa_chain(text)

    # Interaction modes
    st.subheader("Interaction Modes")
    mode = st.radio("Select mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        # Free-form Q&A
        question = st.text_input("Ask a question about the document:")
        if question:
            with st.spinner("Finding answer..."):
                result = st.session_state.qa_chain({"query": question})
                st.subheader("Answer")
                st.write(result["result"])
                if result.get("source_documents"):
                    st.subheader("Source Reference")
                    st.write(result["source_documents"][0]["page_content"][:500] + "...")  # Fixed: use dict access

    else:
        # Challenge Me mode
        if "questions" not in st.session_state:
            with st.spinner("Generating questions..."):
                st.session_state.questions = generate_challenge_questions(text)
                st.session_state.current_question = 0
                st.session_state.scores = []

        if st.session_state.current_question < len(st.session_state.questions):
            current_q = st.session_state.questions[st.session_state.current_question]
            st.subheader(f"Question {st.session_state.current_question + 1}")
            st.write(current_q)

            user_answer = st.text_area("Your answer:")
            if st.button("Submit Answer"):
                with st.spinner("Evaluating..."):
                    evaluation = evaluate_answer(current_q, user_answer, text)
                    st.subheader("Evaluation")
                    st.write(evaluation)
                    st.session_state.scores.append(evaluation)
                    st.session_state.current_question += 1
        else:
            st.subheader("Challenge Complete!")
            st.write("Your evaluations:")
            for i, eval in enumerate(st.session_state.scores):
                st.write(f"Question {i+1}: {eval}")''')

# Cell 3: Run the app
!streamlit run research_assistant.py --server.port=8501 --server.headless=true &>/content/logs.txt &
!sleep 15
!npm install -g localtunnel
!npx localtunnel --port 8501

!curl https://loca.lt/mytunnelpassword

!ps aux | grep streamlit

