export async function getWeeklyReview() {

  const response =
    await fetch(
      "http://127.0.0.1:8000/review/weekly"
    );

  return await response.json();
}

const API_URL = "http://127.0.0.1:8000";

async function request(url) {
  const response = await fetch(`${API_URL}${url}`);

  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }

  return response.json();
}

export const getTasks = () => request("/tasks");
export const getStats = () => request("/stats");
export const getDashboard = () => request("/dashboard");