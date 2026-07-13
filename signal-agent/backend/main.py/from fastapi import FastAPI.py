from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "online",
        "agent": "Signal Agent"
    }