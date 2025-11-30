# llm.py
import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("Please set GOOGLE_API_KEY in your .env file")


# configure the client
genai.configure(api_key=API_KEY)


# helper for simple text generation
def llm_call(prompt: str, model: str = "gemini-1.5-flash", max_output_tokens: int = 1024):
    # Uses the Generative API to produce text
    response = genai.generate_text(model=model, prompt=prompt, max_output_tokens=max_output_tokens)
    # The library may return slightly different shapes; attempt to read text
    # If the library returns .text attribute, return that, else stringify
    if hasattr(response, "text"):
        return response.text
    return str(response)
