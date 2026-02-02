import React, { useEffect, useState, useRef } from "react";
import api from "../api/axios";
import Summary from "../components/Summary";
import Charts from "../components/Charts";
import DatasetHistory from "../components/DatasetHistory";
import PDFDownloadButton from "../components/PDFReport";
import "../style/dashboard.css";

function Dashboard({ onLogout }) {
  const [datasets, setDatasets] = useState([]);
  const fileInputRef = useRef(null);

  const fetchHistory = async () => {
    const res = await api.get("history/");
    setDatasets(res.data);
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("csv_file", file);

    try {
      await api.post("upload/", formData);
      await fetchHistory();
    } catch (err) {
      alert("Upload failed");
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    onLogout();
  };

  return (
    <div className="dashboard">
      {/* Top bar */}
      <div className="top-bar">
        <h2>Dashboard</h2>
        <div className="actions">
          <button onClick={() => fileInputRef.current.click()}>+ New Upload</button>
          <button onClick={handleLogout} className="logout">
            Logout
          </button>
        </div>
      </div>

      {/* File input */}
      <input
        type="file"
        accept=".csv"
        ref={fileInputRef}
        style={{ display: "none" }}
        onChange={handleUpload}
      />

      {/* If no datasets */}
      {datasets.length === 0 && (
        <div className="card">
          <p>No datasets uploaded yet.</p>
          <button onClick={() => fileInputRef.current.click()}>+ Upload CSV</button>
        </div>
      )}

      {/* Latest Dataset */}
      {datasets.length > 0 && (
        <div className="card latest-dataset">
          <h3>Latest Dataset</h3>
          <p>
            Uploaded on: <span>{datasets[0].uploaded_at}</span>
          </p>
          <PDFDownloadButton datasetId={datasets[0].id} />
        </div>
      )}

      {/* Summary & Charts */}
      {datasets.length > 0 && (
        <>
          <Summary data={datasets[0]} />
          <Charts data={datasets[0]} />
        </>
      )}

      {/* Dataset History */}
      {datasets.length > 0 && <DatasetHistory datasets={datasets} />}
    </div>
  );
}

export default Dashboard;
