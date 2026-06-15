class DocumentProcessor:

    def clean(self, text):
        return ' '.join(text.split())

    def chunk(self, text, size=500):
        return [text[i:i+size] for i in range(0, len(text), size)]

    def process(self, text):
        cleaned = self.clean(text)
        return self.chunk(cleaned)

    def metadata(self, text):
        return {'length': len(text)}
