import asyncio
import json

from fastapi import FastAPI

app = FastAPI()


@app.post("/search")
async def search():
    await asyncio.sleep(30)
    with open('response_a.json') as f:
        data = json.load(f)
    return data
