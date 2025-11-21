# TitanIA: Enterprise AI Reasoning Platform

TitanIA is a full-stack AI platform designed to demonstrate advanced reasoning capabilities using **RAG (Retrieval-Augmented Generation)** and **Multi-Agent Systems**. It simulates an enterprise environment where documents are ingested, analyzed by a team of AI agents, and used to make data-driven decisions with a complete audit trail.

![TitanIA Dashboard](https://via.placeholder.com/800x400?text=TitanIA+Dashboard+Preview)
*(Replace with actual screenshot)*

## 🚀 Features

*   **📄 Document Ingestion Pipeline**: Upload PDF, TXT, or CSV files. The system chunks, embeds, and indexes them into a Vector Database (**ChromaDB**).
*   **🧠 RAG Engine**: Advanced retrieval using Semantic Search and **Cross-Encoder Re-ranking** for high relevance.
*   **🤖 Multi-Agent System (LangGraph)**:
    *   **Research Agent**: Gathers facts from the knowledge base.
    *   **Risk Agent**: Analyzes potential risks and compliance issues.
    *   **Decision Agent**: Synthesizes information to provide a final recommendation.
    *   **Audit Agent**: Logs every step of the reasoning process for transparency.
*   **🖥️ Modern Frontend**: A clean, responsive dashboard built with **React** and **TailwindCSS**.
*   **🔌 FastAPI Backend**: Robust Python API handling asynchronous tasks and agent orchestration.

## 🛠️ Tech Stack

*   **Backend**: Python, FastAPI, LangChain, LangGraph, ChromaDB, Sentence-Transformers.
*   **Frontend**: React (Vite), TailwindCSS, Axios.
*   **AI/ML**: HuggingFace Embeddings (`all-MiniLM-L6-v2`), Cross-Encoders (`ms-marco-MiniLM-L-6-v2`).

## 📦 Installation & Setup

### Prerequisites
*   Python 3.9+
*   Node.js 16+

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/TitanIA.git
cd TitanIA
```

### 2. Backend Setup
```bash
cd backend
# Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```
The backend will start at `http://localhost:8000`.

### 3. Frontend Setup
```bash
cd frontend
# Install dependencies
npm install

# Run the development server
npm run dev
```
The frontend will start at `http://localhost:5173`.

## 🎮 Usage

1.  Open the dashboard at `http://localhost:5173`.
2.  **Upload a Document**: Use the upload section to add a PDF or text file to the knowledge base.
3.  **Ask a Question**: Type a query in the "Ask TitanIA" box (e.g., *"What are the key risks in this document?"*).
4.  **View Results**: Watch as the agents process your request and display the Final Decision, Risk Analysis, and Audit Log.

## 📂 Project Structure

```
TitanIA/
├── backend/            # FastAPI Server & AI Logic
│   ├── app/
│   │   ├── agents/     # LangGraph Agent Definitions
│   │   ├── rag/        # Vector Store & Retrieval Logic
│   │   ├── ingestion/  # Document Loaders & Chunking
│   │   └── main.py     # API Entry Point
│   └── requirements.txt
└── frontend/           # React Application
    ├── src/
    │   ├── components/ # UI Components
    │   └── App.jsx     # Main Layout
    └── package.json
```

## 🛡️ License

This project is open-source and available under the MIT License.
