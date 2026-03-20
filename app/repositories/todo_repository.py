from app.models.todo_model import Todo
from app.config.db import SessionLocal

class TodoRepository:
    def get_all(self):
        db = SessionLocal()
        try:
            return db.query(Todo).all()
        finally:
            db.close()
        
    def create(self, title):
        db = SessionLocal()
        try:
            todo = Todo(title=title)
            db.add(todo)
            db.commit()
            db.refresh(todo)
            return todo
        finally:
            db.close()