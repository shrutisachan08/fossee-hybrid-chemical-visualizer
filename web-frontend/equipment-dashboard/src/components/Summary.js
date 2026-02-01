import React from "react";
//import api from "../api/axios";
function Summary({ data }) {
  return (
    <div>
      <h3>Summary</h3>
      <p>Total Equipment: {data.total_equipment}</p>
      <p>Average Flowrate: {data.avg_flowrate}</p>
      <p>Average Pressure: {data.avg_pressure}</p>
      <p>Average Temperature: {data.avg_temperature}</p>
      <h4>Type Distribution</h4>
      <ul>
        {Object.entries(data.type_distribution).map(([type, count]) => (
          <li key={type}>{type}: {count}</li>
        ))}
      </ul>
    </div>
  );
}

export default Summary;
