import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


def call_llm(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content