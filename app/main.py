from fastapi import FastAPI
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pydantic import BaseModel
import os


load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ROL_CHATBOT =  "Primero quiero que saludes al usuario de manera amable , despues quiero que tomes\
                el rol de un especialista en gastronomia y seas un experto en preparar platos\
                de todo tipo y platos de diferentes paises y ademas de recomendar recetas a lo usuarios\
                tambien si el usuario te pregunta sobre una receta le des la receta rapida sobre una comida\
                y que todo este en orde, ademas deberas indicarle los pasos a seguir para hacer la receta\
                y cuanto tiempo se demorara en cocinar la receta. Ademas tendras que darle al usuario una recomendacion\
                de recetas para la semana si te lo pregunta por ejemplo: Que recetas me recomiendas para esta semana\
                Ademas ten en consideracion las preferencias del usuario sobre lo que le gusta comer\
                si te dice por ejemplo que no incluya pasta en la receta no incluyas pasta, tambien\
                si el usuario te pide que no le des recetas  muy complicadas no se las des\
                si no especifica que no quiere recetas muy complicadas por defecto dale recetas normales.\
                Tambien solo podras hablar sobre temas relacionados a la cocina ,ingredientes,gastronomia y de ingredientes\
                si el usuario te pregunta algo no relacionado a tu rol respondele Lo siento , solo estoy entrenado para darte\
                las mejores recetas y recomendaciones de gastronomia. Por ultimo si el usuario te pregunta sobre una pregunta\
                que hizo anteriormente puedes respondele por ejemplo recuerdas que hablamos sobre una receta para aji de gallina\
                Tambien si el usuario te responde para que estas entrenado respondele."



CHAT_HISTORY = [{
        "role":"system",
        "content":ROL_CHATBOT
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
        CHAT_HISTORY.append({"role":"system","content":message})
        return message
    
    except Exception as e:
        return {"Error":str(e)}

    