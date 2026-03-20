import { useEffect, useState } from "react";
import "./App.css";

type Todo = {
  id: number;
  title: string;
  completed: boolean;
};

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [title, setTitle] = useState("");

  // 👉 gọi API lấy danh sách
  const fetchTodos = async () => {
    try {
      const res = await fetch("http://localhost:5000/todos");
      const data = await res.json();
      setTodos(data);
    } catch (err) {
      console.error("Error fetching todos:", err);
    }
  };

  // 👉 gọi API tạo todo
  const createTodo = async () => {
    if (!title.trim()) return;

    try {
      await fetch("http://localhost:5000/todos", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title }),
      });

      setTitle("");
      fetchTodos(); // reload list
    } catch (err) {
      console.error("Error creating todo:", err);
    }
  };

  // 👉 load lần đầu
  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div className="container">
      <h1>Todo App 🚀</h1>

      <div className="input-group">
        <input
          type="text"
          placeholder="Nhập todo..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button onClick={createTodo}>Add</button>
      </div>

      <ul className="todo-list">
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.title} {todo.completed ? "✅" : ""}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;