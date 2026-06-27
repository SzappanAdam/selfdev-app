import { completeTask, deleteTask } from "../services/api";

function TaskList({ tasks }) {
  tasks.map((task) => (
    <div key={task.id} className="task-card">
      <h3>
        {task.done ? "✅" : "⬜"} {task.title}
      </h3>
        <TaskList
        tasks={tasks}
        reload={loadTasks}
        />
      <p>
        Priority:
        <b>{task.priority}</b>
      </p>

      <p>
        Category:
        {task.category}
      </p>

      <p>
        Due:
        {task.due_date || "-"}
      </p>

      <div className="task-buttons">
        <button
          onClick={async () => {
            await completeTask(task.id);

            reload();
          }}
        >
          Complete
        </button>

        <button
          onClick={async () => {
            await deleteTask(task.id);

            reload();
          }}
        >
          Delete
        </button>
      </div>
    </div>
  ));
}

export default TaskList;
