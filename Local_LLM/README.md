# Fetch String Context with LangChain and Streamlit

This project demonstrates how to build a conversational context-fetching application using LangChain, Streamlit, and the CTransformers library. The application takes a user query and generates a JSON response with structured information categorized into "who," "what," and "category."

---

## Features
- Utilizes a **Local-LLM** via CTransformers for causal language modeling.
- Fetches structured information from user queries in a JSON format.
- Simple and interactive user interface built using Streamlit.
- On-the-fly conversational memory management with LangChain.

---

## Prerequisites

Before running the application, ensure you have the following installed:

1. Python 3.10 or later
2. Required Python libraries:
    - `langchain`
    - `streamlit`
    - `ctransformers`
    - `os`
    - `langchain-community`

---

## Installation

1. **Clone the Repository:**

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Model Files:**
   - Download the required model files (e.g., `mistral-7b-instruct-v0.1.Q2_K.gguf`) from [TheBloke Models](https://huggingface.co/TheBloke) and place them in the `./model` directory.

---

## Usage

1. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the Application:**
   - Enter a query in the text area.
   - Click the "Fetch" button.
   - The application will process the query and return a structured JSON response.

