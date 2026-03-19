class Memory:
    def __init__(self):
        self.short_term = []

    def add(self, event):
        self.short_term.append(event)
        if len(self.short_term) > 10:
            self.short_term.pop(0)

    def get_summary(self):
        return " | ".join(self.short_term)
