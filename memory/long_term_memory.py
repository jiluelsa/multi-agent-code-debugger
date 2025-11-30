class MemoryBank:
    def __init__(self):
        self.records = []

    def store(self, data):
        self.records.append(data)

    def summarize(self):
        return f"Stored {len(self.records)} items of memory."
