from fastapi import FastAPI

app = FastAPI(title="Order Service",version="0.1.0")

@app.get("/")
def root() -> dict[str,str]:
    return {"service":"order-service","version":"0.1.0"}

@app.get("/health/live")
def health_live() -> dict[str,str]:
    return {"status":"alive"}

@app.get("/health/ready")
def health_ready() -> dict[str,str]:
    return {"status":"ready"}

@app.get("/orders/{order_id}")
def get_order(order_id: str) -> dict[str, str]:
    # Placeholder implementation - replace with actual order retrieval logic
    return {"order_id": order_id, "status": "pending"}