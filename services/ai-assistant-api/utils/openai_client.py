import os
from openai import OpenAI
from dotenv import load_dotenv

# load .env variables from the project root
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(message: str, business_id: str) -> str:
    """
    Basic wrapper around OpenAI chat completion.
    Later we can inject full business config here.
    """
    system_prompt = f"""
    You are the AI receptionist for business ID: {business_id}.
    Answer professionally, clearly, and concisely.
    Ask follow-up questions if needed to help the customer.
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
    )

    return completion.choices[0].message.content
