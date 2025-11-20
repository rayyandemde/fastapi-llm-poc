# FastAPI LLM Text Generator (PoC)

A bare-bones Proof of Concept (PoC) demonstrating a full-stack integration between a **FastAPI** backend and a vanilla **JavaScript** frontend, powered by a local Hugging Face LLM (`Distilled-GPT2`).

**⚠️ Purpose:**
This project is **not** intended to be a production-ready consumer application or a UI design showcase. Its sole purpose is to demonstrate:
1.  **FastAPI Architecture:** Setting up API endpoints, Pydantic models, and static file mounting.
2.  **Full-Stack Communication:** Handling asynchronous `fetch` requests from a frontend to a Python backend.
3.  **ML Integration:** Loading and serving a Hugging Face `pipeline` within an API context.

## Tech Stack
*   **Backend:** Python 3.10+, FastAPI, Uvicorn
*   **ML Engine:** Hugging Face Transformers, PyTorch
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript (No frameworks)

## Project Structure
```text
/
├── main.py           # The FastAPI application & ML pipeline
├── requirements.txt  # Python dependencies
└── static/           # Frontend assets
    ├── index.html    # Main UI
    ├── script.js     # Frontend logic (API calls)
    └── style.css     # Basic styling
```

## How to Run Locally

1.  **Clone and open the repository**
      ```bash
        git clone https://github.com/YOUR_USERNAME/fastapi-llm-poc.git
        cd fastapi-llm-poc
      ```

2.  **Create and activate the virtual environment**
      ```bash
        python -m venv .venv
        source .venv/bin/activate  # On Windows: .venv\Scripts\activate
      ```

3.  **Install dependencies**
      ```bash
        pip install -r requirements.txt
      ```

4.  **Run the server**
      ```bash
        uvicorn main:app --reload
      ```

5.  **Access the App**
    * UI: Open `http://127.0.0.1:8000` in your browser.
    * API Docs: Open `http://127.0.0.1:8000/docs`.
