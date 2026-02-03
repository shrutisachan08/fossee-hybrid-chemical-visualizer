import sys
import requests
import api
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QFileDialog, QVBoxLayout, QTextEdit,
    QLineEdit, QListWidget, QMessageBox
)

from api import login, upload_csv, fetch_dataset_history
from charts import PieChart


class EquipmentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Analyzer")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.handle_login)

        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(login_btn)

        upload_btn = QPushButton("Upload CSV")
        upload_btn.clicked.connect(self.upload_file)
        layout.addWidget(upload_btn)

        self.summary_box = QTextEdit()
        self.summary_box.setReadOnly(True)
        layout.addWidget(self.summary_box)

        self.chart_container = QVBoxLayout()
        layout.addLayout(self.chart_container)

        self.history_label = QLabel("Last 5 Datasets")
        self.history_list = QListWidget()
        layout.addWidget(self.history_label)
        layout.addWidget(self.history_list)

        self.download_pdf_btn = QPushButton("Download PDF of Selected Dataset")
        self.download_pdf_btn.clicked.connect(self.download_selected_pdf)
        layout.addWidget(self.download_pdf_btn)

        self.setLayout(layout)

    def handle_login(self):
        try:
            login(self.username.text(), self.password.text())
            self.summary_box.setText("Login successful!")
            self.load_history()
        except Exception as e:
            self.summary_box.setText(f"Login failed:\n{e}")

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        try:
            data = upload_csv(file_path)
            self.display_summary(data)
            self.display_chart(data["type_distribution"])
            self.load_history()
        except Exception as e:
            self.summary_box.setText(f"Upload failed:\n{e}")
            
    def display_summary(self, data):
        text = (
            f"Total Equipment: {data['total_equipment']}\n"
            f"Average Flowrate: {data['avg_flowrate']}\n"
            f"Average Pressure: {data['avg_pressure']}\n"
            f"Average Temperature: {data['avg_temperature']}\n\n"
            "Type Distribution:\n"
        )

        for k, v in data["type_distribution"].items():
            text += f"• {k}: {v}\n"

        self.summary_box.setText(text)

    def display_chart(self, distribution):
        while self.chart_container.count():
            item = self.chart_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        chart = PieChart(distribution)
        self.chart_container.addWidget(chart)

    def load_history(self):
        try:
            datasets = fetch_dataset_history()
            self.history_list.clear()

            for ds in datasets:
                self.history_list.addItem(
                    f"ID: {ds['id']} | "
                    f"Uploaded: {ds['uploaded_at']} | "
                    f"Total Equipment: {ds['total_equipment']}"
                )
        except Exception:
            self.history_list.addItem("Failed to load history")

    def download_selected_pdf(self):
        selected_item = self.history_list.currentItem()

        if not selected_item:
            QMessageBox.warning(self, "No Selection", "Please select a dataset first.")
            return

        dataset_id = selected_item.text().split("|")[0].replace("ID:", "").strip()
        self.download_pdf(dataset_id)

    def download_pdf(self, dataset_id):
        if not api.TOKEN:
            QMessageBox.warning(self, "Not logged in", "Please login first.")
            return

        url = f"http://localhost:8000/api/datasets/{dataset_id}/report/"
        headers = {"Authorization": f"Bearer {api.TOKEN}"}

        response = requests.get(url, headers=headers, stream=True)

        if response.status_code == 200:
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save PDF",
                f"dataset_{dataset_id}_report.pdf",
                "PDF Files (*.pdf)"
            )

            if save_path:
                with open(save_path, "wb") as f:
                    for chunk in response.iter_content(8192):
                        f.write(chunk)

                QMessageBox.information(self, "Success", "PDF downloaded successfully!")
        else:
            QMessageBox.warning(
                self,
                "Error",
                f"Failed to download PDF\n"
                f"Status: {response.status_code}\n{response.text}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentApp()
    window.show()
    sys.exit(app.exec_())