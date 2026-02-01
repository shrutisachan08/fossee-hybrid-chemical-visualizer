import React from "react";
import CSVUpload from "../components/CSVUpload";
//import api from "../api/axios";
function Home() {
  return (
    <div style={{ maxWidth: "600px", margin: "50px auto", textAlign: "center" }}>
      <h1>Welcome to Equipment Dashboard</h1>
      <p>Upload your CSV file to view equipment statistics, charts, and reports.</p>
      
      {/* CSV Upload Component */}
      <CSVUpload />
    </div>
  );
}

export default Home;
