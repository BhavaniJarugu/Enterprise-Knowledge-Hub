from dataclasses import dataclass

@dataclass
class Document:
    id: str
    name: str
    content: str

@dataclass
class SearchResult:
    source: str
    content: str

@dataclass
class KnowledgeResponse:
    answer: str
