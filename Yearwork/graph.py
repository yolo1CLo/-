import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class TableWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Input Table')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(10)  
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['X', 'Y'])
        
        self.layout.addWidget(self.table)

        self.button = QPushButton('Generate Graph')
        self.button.clicked.connect(self.generate_graph)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def generate_graph(self):
        data = []
        for row in range(self.table.rowCount()):
            x_item = self.table.item(row, 0)
            y_item = self.table.item(row, 1)
            if x_item and y_item:
                try:
                    x = float(x_item.text())
                    y = float(y_item.text())
                    data.append((x, y))
                except ValueError:
                    pass
        
        self.save_data_to_file(data)
        from PyQT import GraphGenerator
        graph_generator = GraphGenerator('data.txt')
        graph_generator.plot_graph()
    
    def save_data_to_file(self, data):
        with open('data.txt', 'w') as f:
            for x, y in data:
                f.write(f"{x},{y}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWindow()
    window.show()
    sys.exit(app.exec_())