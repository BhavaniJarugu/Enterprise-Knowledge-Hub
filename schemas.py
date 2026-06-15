from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str

class ChatRequest(BaseModel):
    question: str

class UploadRequest(BaseModel):
    filename: str

class SearchResponse(BaseModel):
    results: list
