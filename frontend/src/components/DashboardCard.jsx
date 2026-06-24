function DashboardCard({
    title,
    value
}) {
    return (
        <div
            style={{
                border: "1px solid #ccc",
                borderRadius: "10px",
                padding: "20px",
                minWidth: "200px"
            }}
        >
            <h3>{title}</h3>
            <h2>{value}</h2>
        </div>
    );
}

export default DashboardCard;

export async function getInsights() {

    const response =
        await fetch(
            "http://127.0.0.1:8000/insights"
        );

    return await response.json();
}