from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de dados
class Item(BaseModel):
    nome: str
    descricao: str = None
    preco: float

# Armazenamento em memória
itens: List[Item] = []

@app.get("/")
def boas_vindas():
    return {"mensagem": "Bem-vindo à API FastAPI!"}

@app.get("/itens", response_model=List[Item])
def listar_itens():
    return itens

@app.post("/itens", response_model=Item)
def criar_item(item: Item):
    itens.append(item)
    return item

@app.put("/itens/{item_id}", response_model=Item)
def atualizar_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(itens):
        raise HTTPException(status_code=404, detail="Item não encontrado")
    itens[item_id] = item
    return item

@app.delete("/itens/{item_id}")
def deletar_item(item_id: int):
    if item_id < 0 or item_id >= len(itens):
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del itens[item_id]
    return {"mensagem": "Item deletado"}

# Para rodar: uvicorn starter-code:app --reload
