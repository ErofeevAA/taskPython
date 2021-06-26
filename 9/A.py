import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt5.QtGui import QColor
import csv


class Table(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 1005, 554)
        self.lay = QHBoxLayout()
        self.table = QTableWidget()
        self.lay.addWidget(self.table)
        self.setLayout(self.lay)
        self.set_table()

    def set_table(self):
        with open('rate.csv', encoding="utf8") as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            title = next(reader)
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount() + 1)
                cur_sum = 0.0
                for j in range(1, len(row)):
                    if row[j]:
                        cur_sum += float(row[j].replace(',', '.'))
                cur_sum /= 10
                color = QColor('green')
                if cur_sum < 90:
                    color = QColor(244, 169, 0)
                if cur_sum < 80:
                    color = QColor('red')
                if cur_sum < 60:
                    color = QColor('black')
                for j in range(0, len(row)):
                    self.table.setItem(i, j, QTableWidgetItem(row[j]))
                    self.table.item(i, j).setBackground(QColor(color))
                self.table.setItem(i, len(title) - 1, QTableWidgetItem(str(cur_sum)))
                self.table.item(i, len(title) - 1).setBackground(QColor(color))
            self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    sys.exit(app.exec())
