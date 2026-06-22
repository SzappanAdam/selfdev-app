function InsightPanel({
    insights
}) {

    return (

        <div>

            <h2>
                Coach Insights
            </h2>

            {insights.map(
                (insight, index) => (

                <p key={index}>
                    {insight}
                </p>

            ))}

        </div>
    )
}

export default InsightPanel;