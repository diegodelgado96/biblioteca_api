from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Prueba_conexión():
    return {"message": "Bienvenido a la API de la Biblioteca"}