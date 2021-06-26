import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout
import sqlite3


class Table(QWidget):
    def __init__(self, genre):
        con = sqlite3.connect("films.db")
        cur = con.cursor()
        genre_id = cur.execute(f"""SELECT id FROM genres
            WHERE title = '{genre}';""").fetchone()[0]
        film = cur.execute(f"""SELECT title FROM Films WHERE genre = {genre_id} ;""").fetchmany(10)
        super().__init__()

        self.setGeometry(70, 10, 300, 555)
        self.lay = QHBoxLayout()
        self.table = QTableWidget()
        self.lay.addWidget(self.table)
        self.setLayout(self.lay)
        self.set_table(film)
        cur.close()

    def set_table(self, film):
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Films"])
        self.table.setRowCount(0)
        for i, row in enumerate(film):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(elem))
            self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table(input())
    ex.show()
    sys.exit(app.exec())
