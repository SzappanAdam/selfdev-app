import { useEffect, useState } from "react";

import Header from "../components/Header";
import Sidebar from "../components/Sidebar";
import DashboardCard from "../components/DashboardCard";
import TaskList from "../components/TaskList";
import WeeklyReview from "../components/WeeklyReview";
import InsightPanel from "../components/InsightPanel";

import {
    getTasks,
    getDashboard,
    getWeeklyReview
} from "../services/api";

function Dashboard() {

    const [tasks, setTasks] = useState([]);
    const [dashboard, setDashboard] = useState(null);
    const [review, setReview] = useState([]);

    useEffect(() => {

        loadTasks();

    }, []);

    async function loadTasks() {
        const data = await getTasks();
        setTasks(data);
    }

    return (

        <div className="app">

            <Sidebar />

            <div className="content">

                <Header />

                {dashboard && (

                    <div className="cards">

                        <DashboardCard
                            title="Tasks"
                            value={dashboard.total_logs}
                        />

                        <DashboardCard
                            title="Completion"
                            value={`${dashboard.completion_rate}%`}
                        />

                        <DashboardCard
                            title="Habits"
                            value={dashboard.active_habits}
                        />

                    </div>

                )}

                <TaskList tasks={tasks} />

                <WeeklyReview summary={review} />

                <InsightPanel />

            </div>

        </div>

    );

}

export default Dashboard;