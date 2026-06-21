import { useEffect, useState } from "react";
import { getTasks } from "./services/api";

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    async function loadTasks() {
      const data = await getTasks();
      setTasks(data);
    }

    loadTasks();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>SelfDev Dashboard</h1>

      <h2>Tasks</h2>

      {tasks.length === 0 ? (
        <p>Nincs feladat.</p>
      ) : (
        tasks.map(task => (
          <div key={task.id}>
            {task.done ? "✅" : "⬜"} {task.title}
          </div>
        ))
      )}
    </div>
  );
}

export default App;