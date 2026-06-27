import { useEffect, useState } from "react";
import { getInsights } from "../services/api";

function InsightPanel() {

    const [insights, setInsights] = useState([]);

    useEffect(() => {

        async function load() {

            const data = await getInsights();
            setInsights(data.insights);

        }

        load();

    }, []);

    return (

        <div className="panel">

            <h2>Insights</h2>

            {insights.map((item, index) => (

                <p key={index}>{item}</p>

            ))}

        </div>

    );

}

export default InsightPanel;