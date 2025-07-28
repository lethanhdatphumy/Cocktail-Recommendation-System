from fastapi import FastAPI
from .routers import cocktails

app = FastAPI(title="Cocktail API", version="1.0.0")
app.include_router(cocktails.router, prefix="/cocktails", tags=["Cocktails"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Cocktail API! Visit /docs for documentation."}
