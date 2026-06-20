class ToDo:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        return f"ToDo {self.title} {'✓' if self.completed else '✗'}"

todos1 = ToDo('Buy milk')
todos2 = ToDo('Buy bread')
todos2.mark_done()

print(todos1)
print(todos2)