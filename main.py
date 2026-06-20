class Todo:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True


todos1 = Todo('Buy milk')
todos2 = Todo('Buy bread')
todos2.mark_done()

print(todos1.title)
print(todos1.completed)
print(todos2.title)
print(todos2.completed)