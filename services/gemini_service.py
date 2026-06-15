import os
import google.generativeai as genai
from dotenv import load_dotenv

from utils.logger import logger

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_response(
        user_input,
        system_prompt,
        chat_history):

    try:

        logger.info(user_input)
        history_text = ""

        for msg in chat_history:

            history_text += (
                f"{msg['role']}: "
                f"{msg['content']}\n"
            )

        final_prompt = f"""
{system_prompt}

Conversation History:
{history_text}

Current User Question:
{user_input}
"""

        response = model.generate_content(
            final_prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"