# LLM Zoomcamp Course Work

This repository contains learning materials, notebooks, scripts, and practice exercises for the **LLM Zoomcamp** course by DataTalks.Club. The goal is to build, evaluate, and deploy production-ready LLM-based applications, focusing on Retrieval-Augmented Generation (RAG) pipelines and Agentic workflows.

---

## 🚀 Getting Started

The project uses [uv](https://github.com/astral-sh/uv) for fast, reliable Python package and environment management.

### 1. Prerequisites
Make sure you have `uv` installed. If not, install it using:
```bash
curl -LsSf https://astral-sh.uv.run/install.sh | sh
```

### 2. Setup Environment
Clone the repository, then synchronize the environment and dependencies:
```bash
uv sync
```
This will automatically create a virtual environment (`.venv`) and install all dependencies listed in `pyproject.toml`.

### 3. API Key Configuration
Create a `.env` file in the root directory and add your Gemini API Key (retrieved from Google AI Studio):
```env
GEMINI_API_KEY="your-gemini-api-key-here"
```

---

## 📂 Repository Structure

```text
├── Lessons/
│   └── 01 Agentic RAG.ipynb   # Step-by-step naive and automated RAG pipeline implementation
├── main.py                    # Connection sanity check using Gemini's OpenAI-compatibility layer
├── pyproject.toml             # Project dependencies and configuration
├── uv.lock                    # Locked dependency versions
└── README.md                  # This file
```

---

## 🛠️ Running the Projects

### Connection Test
Verify your API key setup and OpenAI client compatibility layer with Gemini:
```bash
uv run main.py
```

### Jupyter Notebooks
To run the notebooks inside the `Lessons/` directory:
```bash
uv run jupyter notebook
```
Open `Lessons/01 Agentic RAG.ipynb` in the browser to explore building RAG systems from scratch.

---

## 📦 Dependencies
Key packages used in this project:
- **`openai`**: SDK used to query Gemini models via their OpenAI compatibility layer.
- **`google-genai`**: Google's official SDK for Gemini.
- **`minsearch`**: A lightweight text search index for document retrieval in RAG.
- **`python-dotenv`**: Environment variable management.
- **`requests`**: Fetching datasets and course resources.
- **`jupyter`**: Notebook workspace support.
