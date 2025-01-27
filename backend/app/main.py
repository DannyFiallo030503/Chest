from fastapi import FastAPI
from app.routes import example

app = FastAPI()

# Incluye las rutas desde el archivo de rutas
app.include_router(example.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the backend"}
 
