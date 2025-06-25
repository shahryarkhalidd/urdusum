from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()
client = Client("radientsoul88/urdu-summarizer")

class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(req: SummarizeRequest):
    result = client.predict(text=req.text, api_name="/predict")
    return {"summary": result}
