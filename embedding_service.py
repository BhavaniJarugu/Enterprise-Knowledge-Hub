class EmbeddingService:

    def create_embedding(self, text):
        return [float(len(text) % 100)]

    def batch_embeddings(self, chunks):
        return [self.create_embedding(c) for c in chunks]

    def similarity(self, a, b):
        return 1.0 if a == b else 0.5
