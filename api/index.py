from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="FastAPI-on-Vercel")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + uv."}

handler = Mangum(app)      # AWS Lambda handler that Vercel calls
