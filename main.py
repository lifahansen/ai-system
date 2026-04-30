from fastapi import FastAPI
from core.orchestrator import Orchestrator

app = FastAPI()
orch = Orchestrator()

@app.get("/")
def root():
    return {"msg": "AI Test System Running"}

@app.post("/run")
def run(requirement: str):
    return orch.run(requirement)
