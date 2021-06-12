import sys
from PyQt5.QtWidgets import QTextBrowser, QApplication, QWidget, QPushButton, QVBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QTextCursor


class Render(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        layout = QVBoxLayout()
        self.setWindowTitle('HTML')

        self.text_input = QPlainTextEdit(self)
        self.text_out = QTextBrowser()
        self.text_out.setOpenExternalLinks(True)
        self.button = QPushButton('Рендер', self)
        self.button.clicked.connect(self.render)

        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        layout.addWidget(self.text_out)
        self.setLayout(layout)

    def render(self):
        text_out = self.text_input.toPlainText()

        self.text_out.setPlainText('')
        self.text_out.moveCursor(QTextCursor.Start)
        self.text_out.append(text_out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Render()
    ex.show()
    sys.exit(app.exec())
