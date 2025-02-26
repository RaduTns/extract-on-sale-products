from fastapi import FastAPI
from routes import router  # Import the router

app = FastAPI()

app.include_router(router)  # Include the router

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}