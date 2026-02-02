import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

function CSVUpload() {
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file!");
      return;
    }

    const formData = new FormData();
    formData.append("csv_file", file);

    try {
      await api.post("upload/", formData); 
      alert("File uploaded successfully!");
      navigate("/dashboard");
    } catch (err) {
      if (err.response?.status === 401) {
    alert("Session expired. Please login again.");
    localStorage.clear();
    window.location.href = "/login";
  } else {
    alert("Upload failed");
  }
}
  };

  return (
    <div>
      <h2>Upload CSV</h2>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default CSVUpload;
