import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_openai_response(system_prompt, user_prompt):
    """Get a response from OpenAI's text generation API."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    print(completion.choices[0].message.content)


def main():
    system_prompt = "You are a very helpful assitant for learning Python programming."
    user_prompt = input("Enter your prompt to ChatGPT: ")
    get_openai_response(system_prompt, user_prompt)


main()
