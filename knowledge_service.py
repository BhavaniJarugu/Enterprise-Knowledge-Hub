from vector_store import VectorStore

class KnowledgeService:

    def __init__(self):
        self.store = VectorStore()
        self.store.add('HR policy document')
        self.store.add('Employee onboarding guide')

    def search(self, query):
        return self.store.search(query)

    def chat(self, question):
        docs = self.search(question)
        if docs:
            return f'Knowledge answer based on {docs[0]}'
        return 'No relevant information found'
