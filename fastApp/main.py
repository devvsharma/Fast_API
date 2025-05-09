from fastapi import FastAPI
import uvicorn

PORT = 8000
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)