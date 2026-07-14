from fastapi import FastAPI

app = FastAPI(title="Nagpur Safety Map API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Nagpur Safety Map API is running"}
