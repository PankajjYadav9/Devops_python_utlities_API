from fastapi import FastAPI  # importing FASTAPI class
from routers import metrics, aws


app = FastAPI(
    title="Internal Devops Utilities API",
    description="This is  an internal API utilities App for monitoring the system",
    version="1.1.0",
    doc_url="/docs"
)
@app.get("/")
def hello():
    """
    This is Hello API, just for testing
    """
    return {"message": "Hello Gyzz"}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")