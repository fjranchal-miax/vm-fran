from fastapi import FastAPI

app = FastAPI()

@app.get("/echo")
def read_item(name: str):
    return f'"Name": {name}'

@app.get("/suma")
def read_item(primero: int, segundo: int):
    return f'Suma: {primero + segundo}'