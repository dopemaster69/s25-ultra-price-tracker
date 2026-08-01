import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.services.recommendation import RecommendationEngine

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
            "request": request,

            "retailer": retailer,
            "product": info["product"],
            "storage": info["storage"],
            "price": info["price"],
            "updated": info["updated"],

            "analysis": analysis
        }
    )