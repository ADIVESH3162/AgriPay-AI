# AgriPay AI — Hackathon MVP

AgriPay AI is a prototype agricultural marketplace concept that helps farmers compare indicative market prices, discover potential buyers, and manage crop listings and orders. It demonstrates an AI-inspired recommendation workflow and includes a clearly marked PayPal Sandbox integration path.

## Important prototype limitations
- Market prices and buyer profiles in this package are **sample/demo data**, not live quotations or verified buyers.
- The price estimate is a simple baseline calculation for demonstration, not a trained or validated forecasting model.
- PayPal checkout is **not active until you configure your own PayPal Sandbox credentials** and complete the server-side integration described below. The interface must not be represented as having processed real payments.

## Run locally
Requirements: Python 3.10+

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000

## Features in this MVP
- Farmer dashboard and sample crop listings
- Crop price estimate using transparent demo baseline logic
- Market comparison with indicative sample values
- Buyer matching based on crop and quantity
- Order/payment status demo screen
- Responsive interface

## PayPal Sandbox integration
1. Create a PayPal Developer account at https://developer.paypal.com/
2. Create a Sandbox REST app and obtain Client ID and Secret.
3. Keep credentials on the server only; never put the Secret in browser JavaScript or commit it to GitHub.
4. Implement server-side order creation and capture using the official PayPal Orders API:
   https://developer.paypal.com/docs/api/orders/v2/
5. Set `PAYPAL_CLIENT_ID`, `PAYPAL_CLIENT_SECRET`, and `PAYPAL_BASE_URL=https://api-m.sandbox.paypal.com` as environment variables.
6. Test with Sandbox buyer and seller accounts. Only label a transaction paid after PayPal confirms capture on the server.

This starter intentionally does not claim payment success or contact PayPal without credentials.

## Project structure
- `main.py` — FastAPI app and demo API routes
- `static/index.html` — application UI
- `static/styles.css` — responsive styling
- `static/app.js` — browser interactions
- `data/demo_markets.json` — clearly labelled sample market data
- `requirements.txt` — Python dependencies

## Suggested demo video
Show the farmer dashboard, select a crop and quantity, compare markets, inspect matched buyers, and explain the PayPal Sandbox integration path. Clearly state which values are sample data and which features are live.
