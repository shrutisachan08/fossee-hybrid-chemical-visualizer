import React from "react";
import jsPDF from "jspdf";
//import api from "../api/axios";
function PDFReport({ data }) {
  const generatePDF = () => {
    const doc = new jsPDF();
    doc.text(`Equipment Dataset Report`, 10, 10);
    doc.text(`Total Equipment: ${data.total_equipment}`, 10, 20);
    doc.text(`Avg Flowrate: ${data.avg_flowrate}`, 10, 30);
    doc.text(`Avg Pressure: ${data.avg_pressure}`, 10, 40);
    doc.text(`Avg Temperature: ${data.avg_temperature}`, 10, 50);

    let y = 60;
    doc.text("Type Distribution:", 10, y);
    y += 10;
    Object.entries(data.type_distribution).forEach(([type, count]) => {
      doc.text(`${type}: ${count}`, 10, y);
      y += 10;
    });

    doc.save("report.pdf");
  };

  return <button onClick={generatePDF}>Generate PDF</button>;
}

export default PDFReport;
