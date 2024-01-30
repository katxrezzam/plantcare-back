from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=API_KEY)

messages = [
    {"role": "system", "content": "Plant diseases care assistant"},
]


def handle_responses(message):
    try:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": message}], model="gpt-3.5-turbo"
        )

        reply = chat_completion.choices[0].message
        if not reply:
            return "Couldn't get response"
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        print(f"An error ocurred getting Assistance response: {e}")
        return "Couldn't get response"
