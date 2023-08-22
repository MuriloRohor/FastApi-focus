from pydantic import BaseModel, validator
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str
    
    @validator("age")
    def check_age(cls, age):
        if age < 0:
            raise ValueError("Idade não pode ser negativa!")
        return age

class Produto(BaseModel):
    name: str
    price: float
    stock: int

    @validator("price")
    def check_age(cls, price):
        if price < 0:
            raise ValueError("Preço não pode ser negativa!")
        return price


@app.post("/users/")
def create_user(user: User):
    return user

@app.post("/produto/")
def create_produto(produto: Produto):
    return produto