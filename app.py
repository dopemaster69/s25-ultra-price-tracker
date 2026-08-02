import json
import traceback

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.services.recommendation import RecommendationEngine
from src.database.history import get_price_history
from main import main

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    with open("latest_prices.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    retailer = list(data["retailers"].keys())[0]
    info = data["retailers"][retailer]

    analysis = RecommendationEngine().analyse()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "retailer": retailer,
            "product": info["product"],
            "storage": info["storage"],
            "price": info["price"],
            "updated": info["updated"],
            "analysis": analysis,
        },
    )


@app.get("/api/history")
async def history():

    return JSONResponse(content=get_price_history())


@app.post("/api/sync")
async def sync():

    try:

        main()

        return {
            "status": "success"
        }

    except Exception as e:

        traceback.print_exc()

        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )