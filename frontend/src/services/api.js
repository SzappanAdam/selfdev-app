const API_URL = "http://127.0.0.1:8000";

export async function getTasks() {
    const res = await fetch(`${API_URL}/tasks`);
    return await res.json();
}

export async function getDashboard() {
    const res = await fetch(`${API_URL}/dashboard`);
    return await res.json();
}

export async function getWeeklyReview() {
    const res = await fetch(`${API_URL}/review/weekly`);
    return await res.json();
}

export async function getInsights() {
    const res = await fetch(`${API_URL}/insights`);
    return await res.json();
}

export async function createTask(task) {
    const response = await fetch("http://127.0.0.1:8000/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(task),
    });

    return await response.json();
}

export async function completeTask(id) {

    await fetch(
        `http://127.0.0.1:8000/tasks/${id}/complete`,
        {
            method: "PUT"
        }
    );

}

export async function deleteTask(id) {

    await fetch(
        `http://127.0.0.1:8000/tasks/${id}`,
        {
            method: "DELETE"
        }
    );

}