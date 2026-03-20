from flask import Flask
from app.controllers.todo_controller import todo_bp
from app.config.db import engine, Base

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

app.register_blueprint(todo_bp)

if __name__ == "__main__":
    app.run(debug=True)