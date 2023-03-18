from fastapi import FastAPI, Request
from pydantic import BaseModel

class PingRequest(BaseModel):
    ping: str
    pong: str

class PingResponse(BaseModel):
    ping: str
    pong: str

app = FastAPI()

@app.get("/ping", response_model=PingResponse)
async def getPing(r: Request):
    return PingResponse(ping="ping", pong="pong")

@app.post("/ping", response_model=PingResponse)
async def postPing(r: Request, ping: PingRequest):
    return PingResponse(ping="ping", pong="pong")

@app.post("/ping", response_model=PingResponse)
async def putPing(r: Request, ping: PingRequest):
    return PingResponse(ping="ping", pong="pong")

@app.delete("/ping", response_model=PingResponse)
async def deletePing(r: Request, ping: PingRequest):
    return PingResponse(ping="ping", pong="pong")
