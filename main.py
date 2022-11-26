from typing import Union

import uvicorn as uvicorn
from fastapi import FastAPI
from models.word import Word

app = FastAPI()

database = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/api/words", status_code=201)
async def read_put(word: Word):
    database.append(word)
    return word

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)