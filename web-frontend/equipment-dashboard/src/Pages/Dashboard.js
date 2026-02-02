import React, { useEffect, useState, useRef } from "react";
import api from "../api/axios";
import Summary from "../components/Summary";
import Charts from "../components/Charts";
import DatasetHistory from "../components/DatasetHistory";

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

  if (!datasets.length) {
    return (
      <>
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <h2>Dashboard</h2>
          <button onClick={handleLogout}>Logout</button>
        </div>

        <button onClick={() => fileInputRef.current.click()}>
          + Upload CSV
        </button>

        <input
          type="file"
          accept=".csv"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={handleUpload}
        />
      </>
    );
  }

  return (
    <>
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "12px" }}>
        <h2>Dashboard</h2>
        <div>
          <button onClick={() => fileInputRef.current.click()}>
            + New Upload
          </button>
          <button onClick={handleLogout} style={{ marginLeft: "8px" }}>
            Logout
          </button>
        </div>
      </div>

      <input
        type="file"
        accept=".csv"
        ref={fileInputRef}
        style={{ display: "none" }}
        onChange={handleUpload}
      />

      <Summary data={datasets[0]} />
      <Charts data={datasets[0]} />
      <DatasetHistory datasets={datasets} />
    </>
  );
}

export default Dashboard;
