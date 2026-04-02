from fastapi import FastAPI , HTTPException 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel , Field
from pathlib import Path
from app.Controller.chatbot_controller import chat_process


BASE_DIR = Path(__file__).resolve().parent
VIEW_DIR = BASE_DIR / "View"

app = FastAPI()

# Configuración CORS para permitir solicitudes desde el frontend
# Configuración CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir a dominios específicos si lo prefieres
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"]
)

# Montar archivos estáticos para servir frontend
app.mount("/static", StaticFiles(directory=str(VIEW_DIR)), name="static")

# Ruta para servir index.html como página principal
@app.get("/")
async def serve_index():
    return FileResponse(VIEW_DIR / "index.html")

class getMessage(BaseModel):
    prompt: str = Field(...,min_length=1)
    session_id: str = Field(...,min_length=1)


@app.post("/bot")
async def chatBot(response_chat: getMessage):
    try:
        message = await chat_process(response_chat.prompt, response_chat.session_id)
        return {"response": message}
    
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

    
    

    