import React from "react";
//import api from "../api/axios";

function DatasetHistory({ datasets }) {
  return (
    <div>
      <h3>Last 5 Datasets</h3>
      <ul>
        {datasets.map((ds) => (
          <li key={ds.id}>
            ID: {ds.id} | Uploaded: {new Date(ds.uploaded_at).toLocaleString()} | Total Equipment: {ds.total_equipment}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DatasetHistory;
