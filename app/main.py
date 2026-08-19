from fastapi import FastAPI

app = FastAPI(title="Countries API", version="1.0.0")

COUNTRIES = [
    "Australia",
    "Brazil",
    "Canada",
    "France",
    "Germany",
    "India",
    "Japan",
    "Mexico",
    "Nigeria",
    "United Kingdom",
    "United States",
]


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Countries API is running"}


@app.get("/countries")
def list_countries() -> dict[str, list[str]]:
    return {"countries": COUNTRIES}
