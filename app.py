from fastapi import FastAPI
from schemas import SearchRequest, ChatRequest
from knowledge_service import KnowledgeService

app = FastAPI(title="Enterprise Knowledge Hub")
service = KnowledgeService()

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.post("/search")
def search(req: SearchRequest):
    return {"results": service.search(req.query)}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"answer": service.chat(req.question)}
