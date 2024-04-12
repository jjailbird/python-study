import time
import asyncio

from fastapi import FastAPI

async def some_library(num: int, something:str):
    s = 0
    for i in range(num):
        print(" something.. : ", something, i)
        await asyncio.sleep(1)
        s += int(something)
    return s

app = FastAPI()

@app.post('/')
async def read_results(something:str):
    s1 = await some_library(5, something)
    return {'data' : 'data', 's1':s1}
