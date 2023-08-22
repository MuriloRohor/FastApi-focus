from fastapi import FastAPI

app = FastAPI()

@app.get('/{age}')
def VerificarIdade(age: int):
    if age > 18:
        return {'message': f'{age} -> Você é maior de idade!'}
    else:
        return {'message': f'{age} -> Você é menor de idade!'}
        
        
    