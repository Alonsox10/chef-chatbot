from fastapi import FastAPI , HTTPException
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pydantic import BaseModel , Field
from pathlib import Path
from loguru import logger
import os


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Falta la API key de openai")

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

System_prompt = Path("prompts/system_prompt.md").read_text(encoding="utf-8")
                
# Historial global de conversación.
# Se usa para mantener contexto en el modelo.
CHAT_HISTORY = [{
        "role":"system",
        "content":System_prompt
}
]

app = FastAPI()

class getMessage(BaseModel):
    prompt: str = Field(...,min_length=1,max_length=650)


@app.post("/bot")
async def chatBot(response_chat: getMessage):
    try:

        logger.info(f"Mensaje recibido: {response_chat.prompt}")

        # Guardamos el mensaje del usuario para mantener contexto de la conversación.
        CHAT_HISTORY.append({"role":"user","content":response_chat.prompt})

        response =  await client.responses.create(
            model="gpt-4o-mini", # Usamos  el modelo gpt-4o-mini para reducir costo y latencia
            input=CHAT_HISTORY,
            temperature=0.5
        )

        message = response.output_text
        CHAT_HISTORY.append({"role":"assistant","content":message})

        logger.info("Respuesta generada correctamente")
        return message
    
    except Exception as e:
        logger.error(f"Error en el chatbot: {e}")
        raise HTTPException(status_code=500,detail="Error interno del servidor")
    
    
    # TODO: mover historial a base de datos cuando implementemos PostgreSQL

    