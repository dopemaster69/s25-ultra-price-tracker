import json
import traceback

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.services.recommendation import RecommendationEngine
from src.database.history import get_price_history
from main import run_collection


# ==========================================
# ATLAS APPLICATION
# ==========================================

app = FastAPI(
    title="ATLAS",
    description="Smart Price Intelligence System",
    version="1.0"
)


# ==========================================
# STATIC FILES
# ==========================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# ==========================================
# TEMPLATES
# ==========================================

templates = Jinja2Templates(
    directory="templates"
)


# ==========================================
# HOME
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    with open(
        "latest_prices.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    retailer = list(
        data["retailers"].keys()
    )[0]

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


# ==========================================
# PRICE HISTORY API
# ==========================================

@app.get("/api/history")
async def history():

    try:

        history_data = get_price_history()

        return JSONResponse(
            content=history_data
        )

    except Exception as e:

        traceback.print_exc()

        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )


# ==========================================
# SYNC API
# ==========================================

@app.post("/api/sync")
def sync():

    print()
    print("=" * 60)
    print("ATLAS SYNC REQUEST RECEIVED")
    print("=" * 60)

    try:

        print("Starting price collection...")

        results = run_collection()

        print("Collection completed successfully.")

        successful = []
        failed = []

        for result in results:

            if result.success:

                successful.append({
                    "retailer": result.retailer,
                    "title": result.title,
                    "storage": result.storage,
                    "colour": result.colour,
                    "price": result.price
                })

                print(
                    f"SUCCESS: "
                    f"{result.retailer} "
                    f"₹{result.price:,}"
                )

            else:

                failed.append({
                    "retailer": result.retailer,
                    "error": result.error
                })

                print(
                    f"FAILED: "
                    f"{result.retailer} "
                    f"{result.error}"
                )

        print("latest_prices.json updated.")

        print("=" * 60)
        print("ATLAS SYNC COMPLETE")
        print("=" * 60)
        print()

        return {
            "status": "success",
            "successful": successful,
            "failed": failed
        }

    except Exception as e:

        print()
        print("=" * 60)
        print("ATLAS SYNC FAILED")
        print("=" * 60)

        traceback.print_exc()

        print("=" * 60)
        print()

        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/api/health")
async def health():

    return {
        "status": "online",
        "service": "ATLAS"
    }