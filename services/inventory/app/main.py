from fastapi import FastAPI

app = FastAPI(title="Inventory Service",version="0.1.0")

@app.get("/")
def root() -> dict[str,str]:
    return {"service":"inventory-service","version":"0.1.0"}

@app.get("/health/live")
def health_live() -> dict[str,str]:
    return {"status":"alive"}

@app.get("/health/ready")
def health_ready() -> dict[str,str]:
    return {"status":"ready"}

@app.get("/products/{product_id}")
def get_product(product_id: str) -> dict[str, str]:
    stock_by_product = {
        "1": "100",
        "2": "200",
    }

    available = stock_by_product.get(product_id, "0")

    return {"product_id": product_id, "available": available}