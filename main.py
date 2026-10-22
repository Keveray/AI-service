from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main(x: int):
    return x 
