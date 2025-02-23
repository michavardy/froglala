from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.get_market_cap import get_market_cap
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
app = FastAPI()

# Allow frontend requests from anywhere (adjust this if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/")
async def serve_index():
    """Serve index.html from /"""
    return FileResponse('src/static/index.html')

@app.get("/get-market-cap")
async def get_market_cap_endpoint():
    """Returns a simulated market cap"""
    return {"market_cap": get_market_cap()}
