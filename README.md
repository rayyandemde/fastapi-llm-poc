# FastAPI LLM Text Generator (PoC)

A lightweight, full-stack prototype demonstrating a **Hybrid AI Architecture**. It bridges a **FastAPI** backend with a **Vanilla JavaScript** frontend, currently running a local Hugging Face model (`GPT-2`) for offline inference.

## The Problem & Real-World Context

**The Challenge: Privacy and Latency in Enterprise AI**

While cloud APIs (like OpenAI or Anthropic) offer immense power, they present challenges for specific enterprise use cases:
1.  **Data Privacy:** Sending sensitive internal data (PII, trade secrets) to external third-party servers is often a compliance violation.
2.  **Latency & Reliability:** Cloud dependencies introduce network latency and potential downtime.
3.  **Cost Control:** High-volume, simple tasks (like summarization or basic drafting) can generate unnecessary API bills.

**The Solution: Local-First Architecture**
This project serves as an architectural blueprint for a **Local-First AI Application**. By embedding a model directly within the application infrastructure, organizations can perform inference on their own hardware. This ensures data never leaves the secure environment and eliminates per-token costs for routine tasks.

**Use Case:**
An internal "Drafting Assistant" for a secure facility. Employees can generate initial drafts of reports or emails completely offline. Future iterations can selectively route complex queries to the cloud only when necessary, optimizing the balance between security, cost, and intelligence.

## How It Works (Input/Output)

1.  **Input:** The user enters a prompt into the web interface.
    *   *Example:* `"The capital city of Italy is Rome. The capital city of Japan is Tokyo. The capital city of Germany is Berlin. The capital city of France is"`
2.  **Processing:** The frontend sends this text asynchronously to the FastAPI backend. The backend feeds it into the `gpt2` model running locally on the server.
3.  **Output:** The model predicts the next statistically likely words, and the result is returned to the UI.
    *   *Result:* `"... The capital city of Germany is Berlin. The capital city of France is Paris. ..."`

## Tech Stack

**Current Implementation:**
*   **Backend:** Python 3.10+, FastAPI, Uvicorn.
*   **ML Engine:** Hugging Face Transformers, PyTorch.
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript (chosen to demonstrate raw API interaction logic without framework abstraction).

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

## Future Roadmap

This project represents the **MVP (Minimum Viable Product)**. The following architectural evolutions are planned:

*   **Frontend Modernization:** Migrating the UI to **Vue.js** to introduce component-based architecture and reactive state management.
*   **Hybrid Model Routing:** Implementing a "Model Gateway" pattern. Simple queries will be routed to the local model (free, fast), while complex reasoning tasks can be optionally routed to external APIs (OpenAI/Claude).
*   **Context Awareness:** Implementing "Session Memory" so the model remembers previous turns in the conversation.
*   **Persistence Layer:** Adding a database (SQLite/PostgreSQL) to save conversation history, allowing users to revisit past chats via a sidebar interface.

## How to Run Locally

1.  **Clone and open the repository**
      ```bash
        git clone https://github.com/rayyandemde/fastapi-llm-poc.git
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
        uvicorn main:app
      ```

5.  **Access the App**
    * UI: Open `http://127.0.0.1:8000` in your browser.
    * API Docs: Open `http://127.0.0.1:8000/docs` to see the automatic Swagger UI.
