from fastapi import FastAPI

app = FastAPI(title="Customer Churn Prediction Service")


@app.get("/health")
def health():
    return {"status": "ok"}
