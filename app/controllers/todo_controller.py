from flask import Blueprint, request, jsonify
from app.services.todo_service import TodoService

todo_bp = Blueprint('todo', __name__)
service = TodoService()

@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    todos = service.get_all_todos()
    return jsonify([
        {"id": t.id, "title": t.title, "completed": t.completed} 
        for t in todos
    ])

@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.json
    todo = service.create_todo(data.get("title"))
    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    })