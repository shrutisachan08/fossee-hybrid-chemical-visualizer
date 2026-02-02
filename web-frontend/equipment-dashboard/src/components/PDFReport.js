import React from "react";

function PDFDownloadButton({ datasetId }) {
  const downloadPDF = async () => {
    const token = localStorage.getItem("access");
    if (!token) {
      alert("You must be logged in to download the PDF");
      return;
    }

    try {
      const response = await fetch(
        `http://localhost:8000/api/datasets/${datasetId}/report/`,
        { headers: { Authorization: `Bearer ${token}` } }
      );

      if (!response.ok) {
        const text = await response.text();
        console.error("Download failed:", response.status, text);
        alert(`Failed to download PDF: ${response.status}`);
        return;
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `dataset_${datasetId}_report.pdf`;
      a.click();
      window.URL.revokeObjectURL(url);
    } catch (err) {
      console.error(err);
      alert("Error downloading PDF");
    }
  };

  return <button onClick={downloadPDF}>Download PDF</button>;
}

export default PDFDownloadButton;
                                                                                                                                              