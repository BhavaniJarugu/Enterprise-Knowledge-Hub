class ChatService:

    def generate_response(self, question, context):
        return f'Answer for {question}'

    def summarize(self, text):
        return text[:200]

    def cite_sources(self, docs):
        return [f'Document {i+1}' for i in range(len(docs))]
