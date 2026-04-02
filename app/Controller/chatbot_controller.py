from openai import AsyncOpenAI
from pathlib import Path
from loguru import logger
from dotenv import load_dotenv
import os
import re
from fastapi import HTTPException
from app.Model.receta_model import obtener_recetas_por_ingredientes
from app.Model.usuario_model import obtener_usuario_por_nombre,crear_usuario


load_dotenv()

#relación session → user_id
session_users = {}


# Inicialización del cliente
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise HTTPException(status_code=400, detail="Falta la API key de OpenAI")

client = AsyncOpenAI(api_key=API_KEY)

# System prompt
SYSTEM_PROMPT = Path("prompts/system_prompt.md").read_text(encoding="utf-8")

# Diccionario que guarda el historial de cada sesión
session_histories: dict[str, list[dict]] = {}


def get_history(user_id: str) :
    """Obtiene o crea el historial para un usuario."""
    if user_id not in session_histories:
        session_histories[user_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    return session_histories[user_id]


async def chat_process(prompt: str, session_id: str):
    try:
        if session_id not in session_users:
            nombre_usuario = prompt.strip()

            # Validar que el nombre solo contenga letras y espacios (2-50 caracteres)
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]{2,50}$', nombre_usuario):
                return "Por favor, ingresa un nombre válido (solo letras, sin números ni caracteres especiales)."

            usuario= obtener_usuario_por_nombre(nombre_usuario)

            #Si no existe el usuario, se crea uno nuevo
            if not usuario:
                user_id = crear_usuario(nombre_usuario)
            else:
                user_id = usuario[0]
                
            #Aqui el bot recuerda el nombre del usuario y lo asocia a la sesión actual
            session_users[session_id] = user_id

            # Inyectar el nombre en el historial para que GPT sepa que ya lo tiene
            bienvenida = f"Bienvenido {nombre_usuario} 👋 ¿Qué receta buscas hoy?"
            history = get_history(str(user_id))
            history.append({"role": "user", "content": nombre_usuario})
            history.append({"role": "assistant", "content": bienvenida})

            return bienvenida
        
        #Obtener el id del usuario en la session actual y su historial
        user_id = session_users[session_id]
        history = get_history(str(user_id))
        history.append({"role":"user","content": prompt})

        prompt_lower = prompt.lower()


        if "pollo" in prompt_lower:
            recetas = obtener_recetas_por_ingredientes("pollo")
            
            #Verificar si se encontraron recetas y extraer los nombres
            if recetas:
                nombres = [receta[1]for receta in recetas]
                respuesta = f"Te recomiendo recetas con pollo {', '.join(nombres[:5])}"
            else:
                respuesta = "Lo siento, no encontre recetas con pollo"

            # guardar respuesta en el historial
            history.append({"role":"assistant","content":respuesta})
            return respuesta

        logger.info(f"[{session_id[:8]}] Mensaje recibido: {prompt}")

        #Si no se encuentra un ingrediente específico, se envía el mensaje a GPT para generar una respuesta

        response = await client.responses.create(
            model="gpt-5.1",
            input=history,
            temperature=0
        )

        message = response.output_text
        history.append({"role": "assistant", "content": message})

        logger.info(f"[{session_id[:8]}] Respuesta generada correctamente")

        return message

    except Exception as e:
        logger.error(f"Error en el chatbot: {e}")
        raise HTTPException(status_code=500, detail="Error del servidor")