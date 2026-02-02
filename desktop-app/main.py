import sys
from api import TOKEN
from api import fetch_dataset_history
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QFileDialog, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit,QListWidget
)
from api import login, upload_csv
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

        self.setLayout(layout)
        self.history_label = QLabel("Last 5 Datasets")
        self.history_list = QListWidget()
        layout.addWidget(self.history_label)
        layout.addWidget(self.history_list)

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
                item_text = (
                    f"ID: {ds['id']} | "
                    f"Uploaded: {ds['uploaded_at']} | "
                    f"Total Equipment: {ds['total_equipment']}"
                )
                self.history_list.addItem(item_text)

        except Exception as e:
            self.history_list.addItem("Failed to load history")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentApp()
    window.show()
    sys.exit(app.exec_())
