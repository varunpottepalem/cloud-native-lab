from fastapi import FastAPI

app = FastAPI(title="Gateway Service",version="0.1.0")

@app.get("/")
def root() -> dict[str,str]:
    return {"service":"gateway-service","version":"0.1.0"}

@app.get("/health/live")
def health_live() -> dict[str,str]:
    return {"status":"alive"}

@app.get("/health/ready")
def health_ready() -> dict[str,str]:
    return {"status":"ready"}