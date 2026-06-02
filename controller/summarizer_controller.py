import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)


def summarize_document(text):

    if not text:
        return "No content found."

    prompt = f"""
You are an AI-powered document intelligence system.

Generate a professional executive summary of the following document.

Requirements:
- Summarize the document in 5-8 meaningful sentences.
- Clearly explain the document's purpose.
- Highlight important information, findings, and conclusions.
- Use professional and formal language.
- Avoid repetition.
- Do not copy text directly from the document.
- Make the summary easy to understand for business users.

Document:
{text[:15000]}
"""

    response = client.models.generate_content(
        model=os.getenv(
            "MODEL_NAME"
        ),
        contents=prompt
    )

    return response.text