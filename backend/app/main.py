from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routes import reports

# Creates the "reports" table inside your SQLite file if it doesn't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nagpur Safety Map API")

# Lets your frontend (running on a different port, e.g. 5501) call this API
# from the browser. Browsers block cross-origin requests by default — this
# explicitly allows it.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reports.router)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Nagpur Safety Map API is running"}
