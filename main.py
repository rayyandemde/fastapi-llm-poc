from os.path import join, dirname, abspath
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.staticfiles import StaticFiles

STATIC_PATH = join(dirname(abspath(__file__)), "static")

print("Loading text-generation model... (This may take a moment on first run)")
GENERATOR = pipeline('text-generation', model='distilgpt2')
print("Model loaded successfully.")

app = FastAPI(
    title="LLM Generation API",
    description="A simple API for text generation with a static frontend.",
    version="1.0.0"
)


class GenerationBody(BaseModel):
    prompt: str


class GenerationResponse(BaseModel):
    generated_text: str


class LabResponse(BaseModel):
    request: str


@app.post("/api/generate", response_model=GenerationResponse, tags=["api"])
async def post_generate(body: GenerationBody):
    """
    Generates text based on a user-provided prompt.
    """
    results = GENERATOR(body.prompt, max_length=35, num_return_sequences=1)
    return results[0]


@app.get("/api/get-test", response_model=LabResponse, tags=["api"])
def get_test():
    """
    Simple get endpoint that returns a structured JSON response.
    """
    return {"request": "GET"}


app.mount("/", StaticFiles(directory=STATIC_PATH, html=True), name="static")
