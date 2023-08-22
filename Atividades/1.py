from fastapi import FastAPI

app = FastAPI()

@app.get("/{nome}")
def ler_nome(nome : str):
    return {"message": f"Olá, {nome}!"}