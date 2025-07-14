## 📖 Project Description

This tool aims to simplify the reading process of lengthy research documents by providing instant summaries, a question-answer interface, and an interactive "Challenge Me" mode. Whether you're a student, researcher, or professional, this assistant helps you **read less but understand more**.

## Screenshots
<img width="1920" height="1020" alt="Screenshot 2025-07-14 093909" src="https://github.com/user-attachments/assets/da29fe69-a0bf-485a-a7a2-ad57196580cb" />

<img width="1920" height="1020" alt="Screenshot 2025-07-14 093932" src="https://github.com/user-attachments/assets/cecc3e28-a3fb-4266-a851-f914aa07b6bb" />

<img width="1902" height="1010" alt="Screenshot 2025-07-14 093958" src="https://github.com/user-attachments/assets/951c53f7-e635-446b-b7a9-427ddd6f0771" />

<img width="1920" height="1020" alt="Screenshot 2025-07-14 094021" src="https://github.com/user-attachments/assets/921c724b-aa9a-437c-884f-4441b49b9b25" />


## Key goals:
- Improve document comprehension.
- Reduce manual reading effort.
- Enable offline GenAI-based assistance without LLM APIs.
- Deliver a smooth and interactive user experience via Streamlit.

---

## ✨ Features

- 📄 Upload & parse PDF or TXT documents
- 🧠 Auto-summarization of long documents
- 💬 Ask natural language questions about the uploaded document
- 🎯 Challenge mode: test your understanding with auto-generated questions
- 📌 No external API or internet required – works completely offline
- ✅ Modular and clean backend code

---

## 📁 Folder Structure

smart-assistant-genai/
│
├── app.py # Streamlit-based UI
│
├── requirements/
│ ├── base.txt # Core app dependencies
│ ├── dev.txt # Developer tools (formatters, linters)
│ ├── all.txt # Combines base + dev dependencies
│
├── sample_docs/
│ └── example.pdf # Example document for testing
│
├── README.md # Complete project overview
└── .gitignore # Files/folders to exclude from Git

---

## ⚙️ Technologies Used

| Component        | Technology             |
|------------------|------------------------|
| 🖥️ Frontend       | Streamlit              |
| 📄 PDF Parsing   | PyPDF2                 |
| 🧠 NLP Tools     | LangChain (community)  |
| 🗃️ Text Splitter  | RecursiveCharacterTextSplitter |
| 🔍 Vector Search | FAISS (optional use)   |

---

## 🛠️ Installation & Setup

### 🔧 1. Clone the repository


git clone https://github.com/rishabh01032003/research-assistant.git
cd smart-assistant-genai
📦 2. Install core dependencies
bash
Copy
Edit
pip install -r requirements/base.txt
For development:


## 🧠 How to Use
Upload a PDF or TXT file using the file uploader.

Read the automatically generated summary.

Choose between:

Ask Anything: Ask any question about the document.

Challenge Me: Answer AI-generated questions and get feedback.

View your evaluations at the end of the challenge.


## 🔮 Future Enhancements (To-Do)
 Integrate real LLM (OpenAI or HuggingFace) for smarter QA

 Extract author names, citations, or sections automatically

 Auto-generate MCQs using transformer-based models

 Add user authentication for saving history

 Deploy app using Streamlit Cloud or Hugging Face Spaces

👨‍💻 Author
Rishabh Singh
B.Tech Student @ NIET Greater Noida
GitHub: @rishabh01032003
Passionate about GenAI, research tools, and building impactful applications.
