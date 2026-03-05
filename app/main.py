from fastapi import FastAPI
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pydantic import BaseModel
from pathlib import Path
import os


load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

System_prompt = Path("prompts/system_prompt.md").read_text(encoding="utf-8")
                

CHAT_HISTORY = [{
        "role":"system",
        "content":System_prompt
}
]


app = FastAPI()

class getMessage(BaseModel):
    prompt: str


@app.post("/bot")
async def chatBot(response_chat: getMessage):
    try:

        CHAT_HISTORY.append({"role":"user","content":response_chat.prompt})

        response =  await client.responses.create(
            model="gpt-4o-mini",
            input=CHAT_HISTORY,
            temperature=0.5
        )

        message = response.output_text
        CHAT_HISTORY.append({"role":"assistant","content":message})
        return message
    
    except Exception as e:
        return {"Error":str(e)}

    