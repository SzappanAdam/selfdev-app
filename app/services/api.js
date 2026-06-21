const API_URL = "http://127.0.0.1:8000";

export async function getTasks() {
    const response = await fetch(`${API_URL}/tasks`);
    return await response.json();
}

export async function getStats() {
    const response = await fetch(`${API_URL}/stats`);
    return await response.json();
}