from app.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self):
        self.repo = TodoRepository()

    def get_all_todos(self):
        return self.repo.get_all()
        
    def create_todo(self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        return self.repo.create(title)