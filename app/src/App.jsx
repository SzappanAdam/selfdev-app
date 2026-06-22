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

import { useEffect, useState } from "react";

import DashboardCard from "./components/DashboardCard";

import {
    getDashboard,
    getTasks
} from "./services/api";

const [dashboard, setDashboard] =
    useState(null);

useEffect(() => {

    async function loadData() {

        const tasksData =
            await getTasks();

        const dashboardData =
            await getDashboard();

        setTasks(tasksData);
        setDashboard(dashboardData);
    }

    loadData();

}, []);

{dashboard && (

<div
    style={{
        display: "flex",
        gap: "20px",
        marginBottom: "30px"
    }}
>

<DashboardCard
    title="Logs"
    value={dashboard.total_logs}
/>

<DashboardCard
    title="Completion Rate"
    value={`${dashboard.completion_rate}%`}
/>

<DashboardCard
    title="Active Habits"
    value={dashboard.active_habits}
/>

</div>

)}

export async function getWeeklyReview() {

    const response =
        await fetch(
            "http://127.0.0.1:8000/review/weekly"
        );

    return await response.json();
}

function WeeklyReview({
    summary
}) {

    return (

        <div>

            <h2>
                Weekly Review
            </h2>

            {summary.map(
                (item, index) => (

                <p key={index}>
                    {item}
                </p>

            ))}

        </div>

    )
}

export default WeeklyReview;