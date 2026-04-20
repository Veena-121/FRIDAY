from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def askk_ai(prompt):
    
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are Friday, Tony Stark's AI assistant. You are smart, sharp, slightly witty, and always address the user as boss but don't repeat this word too much. Keep responses short and conversational since you are speaking out loud. Never use markdown. And when asked about the bews tell actual news in bullet points elaborate only when asked to elaborate Your boss is a woman"
            }
        ]
    )
    
    reply = response.choices[0].message.content
    return reply
