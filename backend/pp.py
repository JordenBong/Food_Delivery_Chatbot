from fastapi import FastAPI

app = FastAPI(debug=True)  # Enable debug mode

@app.get("/")
async def root():
    return {"message": "Hello World"}
