from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json

BASE = Path(__file__).parent
app = FastAPI(title="AgriPay AI", description="Agricultural marketplace MVP")
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")

with open(BASE / "data" / "demo_markets.json", encoding="utf-8") as f:
    MARKETS = json.load(f)

BUYERS = [
    {"name": "FreshMart Foods", "city": "Bengaluru", "crop": "Tomato", "quantity": 1000, "offer": 28, "rating": 4.8, "tag": "Wholesaler"},
    {"name": "GreenLeaf Traders", "city": "Hubballi", "crop": "Tomato", "quantity": 500, "offer": 26, "rating": 4.6, "tag": "Wholesaler"},
    {"name": "AgroFresh Exports", "city": "Mumbai", "crop": "Tomato", "quantity": 2000, "offer": 30, "rating": 4.5, "tag": "Exporter"},
    {"name": "FarmLink Retail", "city": "Belagavi", "crop": "Tomato", "quantity": 600, "offer": 25, "rating": 4.4, "tag": "Retail chain"},
    {"name": "GrainBridge Foods", "city": "Dharwad", "crop": "Maize", "quantity": 1500, "offer": 22, "rating": 4.7, "tag": "Processor"},
    {"name": "Harvest Basket", "city": "Belagavi", "crop": "Onion", "quantity": 800, "offer": 27, "rating": 4.6, "tag": "Retail chain"}
]

@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE / "static" / "index.html").read_text(encoding="utf-8")

@app.get("/api/markets")
def markets(crop: str = "Tomato"):
    return {"notice": "DEMO DATA — not live market prices", "crop": crop,
            "markets": MARKETS.get(crop, MARKETS["Tomato"])}

@app.get("/api/predict")
def predict(crop: str = "Tomato", quantity: int = 500):
    rows = MARKETS.get(crop, MARKETS["Tomato"])
    prices = [x["price"] for x in rows]
    avg = round(sum(prices) / len(prices), 2)
    # Transparent baseline estimate, not a trained forecasting model.
    estimate = round(avg * 1.04, 2)
    return {"crop": crop, "quantity_kg": max(1, quantity), "current_reference_price": avg,
            "indicative_estimate": estimate, "estimated_gross_value": round(estimate * max(1, quantity), 2),
            "method": "Demo baseline: average sample market reference × 1.04",
            "notice": "Illustrative estimate only. Not a validated forecast."}

@app.get("/api/buyers")
def buyers(crop: str = "Tomato", quantity: int = 500):
    matches = [b for b in BUYERS if b["crop"].lower() == crop.lower() and b["quantity"] >= quantity]
    return {"notice": "DEMO buyer profiles — not verified or connected to real buyers", "buyers": matches}

@app.get("/api/health")
def health():
    return {"status": "ok", "app": "AgriPay AI", "mode": "prototype"}
