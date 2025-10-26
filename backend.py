# backend.py
from fastapi import FastAPI, UploadFile
import pandas as pd
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/analyze")
async def analyze(file: UploadFile):
    df = pd.read_excel(file.file)
    text_summary = df.head().to_string()  # very basic
    prompt = f"Here is some data:\n{text_summary}\n\nGive simple recommendations."
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[{"role": "system", "content": prompt}]
    )

    return {"recommendation": response.choices[0].message.content}