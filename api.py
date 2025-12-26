from fastapi import FastAPI
from extractor.extractor import ModuleExtractor

app = FastAPI()
extractor = ModuleExtractor()

@app.get("/extract")
def extract(url: str):
    return extractor.extract(url)
