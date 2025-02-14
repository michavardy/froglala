from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.get_market_cap import get_market_cap
import random

app = FastAPI()

# Serve static files from the 'resources' directory
app.mount("/static", StaticFiles(directory="resources"), name="static")

@app.get("/get-market-cap")
async def get_market_cap():
    """Returns a simulated market cap"""
    market_cap = get_market_cap()
    return f"<script>updateImageSize({market_cap});</script>"
