class VectorStore:

    def __init__(self):
        self.documents = []

    def add(self, text):
        self.documents.append(text)

    def search(self, query):
        return [d for d in self.documents if query.lower() in d.lower()]

    def count(self):
        return len(self.documents)
