# charts.py
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class PieChart(FigureCanvasQTAgg):
    def __init__(self, data):
        fig = Figure(figsize=(5, 4))
        self.ax = fig.add_subplot(111)
        super().__init__(fig)
        self.plot(data)

    def plot(self, data):
        labels = list(data.keys())
        values = list(data.values())

        self.ax.clear()
        self.ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
        self.ax.set_title("Equipment Type Distribution")
        self.draw()
