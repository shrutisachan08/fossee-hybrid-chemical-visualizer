import React from "react";
import CSVUpload from "../components/CSVUpload";
import "../style/home.css";

function Home() {
  return (
    <div className="home-container">
      <div className="home-card">
        <h1>Equipment Dashboard ⚙️</h1>

        <p className="home-subtitle">
          Upload your CSV file to analyze equipment statistics, visualize data,
          and generate insightful reports.
        </p>

        <div className="upload-section">
          <CSVUpload />
        </div>

        <p className="home-footer">
          Supported format: <strong>.csv</strong>
        </p>
      </div>
    </div>
  );
}

export default Home;
