import React from "react";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
//import api from "../api/axios";

ChartJS.register(ArcElement, Tooltip, Legend);

function Charts({ data }) {
  const pieData = {
    labels: Object.keys(data.type_distribution),
    datasets: [
      {
        label: "Equipment Types",
        data: Object.values(data.type_distribution),
        backgroundColor: [
          "#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF", "#FF9F40",
        ],
      },
    ],
  };
  const options = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: "top",
    },
  },
};

  return (
    <div>
      <h3>Equipment Type Distribution</h3>
      <div style={{ height: "400px" }}>
      <Pie data={pieData} options={options} />
    </div>
    </div>
  );
}

export default Charts;
