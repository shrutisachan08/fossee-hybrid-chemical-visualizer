import React, { useEffect, useState } from "react";
import api from "../api/axios";
import Summary from "../components/Summary";
import Charts from "../components/Charts";
import DatasetHistory from "../components/DatasetHistory";

function Dashboard() {
  const [datasets, setDatasets] = useState([]);

  useEffect(() => {
    api.get("history/").then((res) => {
      setDatasets(res.data);
    });
  }, []);

  if (!datasets.length) return <p>Upload CSV to begin</p>;

  return (
    <>
      <Summary data={datasets[0]} />
      <Charts data={datasets[0]} />
      <DatasetHistory datasets={datasets} />
    </>
  );
}

export default Dashboard;
