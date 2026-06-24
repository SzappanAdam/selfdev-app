import { useEffect, useState } from "react";

import DashboardCard from "./components/DashboardCard";
import WeeklyReview from "./components/WeeklyReview";

import {
  getTasks,
  getDashboard,
  getWeeklyReview
} from "./services/api";

function App() {

  const [tasks, setTasks] = useState([]);
  const [dashboard, setDashboard] = useState(null);
  const [review, setReview] = useState([]);

  useEffect(() => {

    async function loadData() {

      const tasksData =
        await getTasks();

      const dashboardData =
        await getDashboard();

      const reviewData =
        await getWeeklyReview();

      setTasks(tasksData);
      setDashboard(dashboardData);
      setReview(reviewData.summary);
    }

    loadData();

  }, []);

  return (

    <div style={{ padding: "20px" }}>

      <h1>SelfDev Dashboard</h1>

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

      <WeeklyReview
        summary={review}
      />

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