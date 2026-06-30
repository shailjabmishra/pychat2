from fastapi import FastAPI

app = FastAPI(
    title = "Pychat V2",
    version= "2.0.0"
)

@app.get("/health")
async def health_check():
    return {
        "status" : "ok"
    }