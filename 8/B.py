import sys
from abc import abstractmethod
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLineEdit, QApplication)
from PyQt5.QtWidgets import QMessageBox


class Button(QPushButton):

    def __init__(self, text, line_edit: QLineEdit):
        super().__init__(text)
        self._text = text
        self._line_edit = line_edit
        self.clicked.connect(self._on_click)

    @abstractmethod
    def _on_click(self):
        pass


class ClearButton(Button):

    def __init__(self, line_edit: QLineEdit):
        super().__init__('AC', line_edit)

    def _on_click(self):
        self._line_edit.setText('')


class DelButton(Button):

    def __init__(self, line_edit: QLineEdit):
        super().__init__('<', line_edit)

    def _on_click(self):
        self._line_edit.setText(self._line_edit.text()[:-1])


class CalculateButton(Button):

    def __init__(self, text, line_edit: QLineEdit):
        super().__init__(text, line_edit)

    def _on_click(self):
        self._line_edit.setText(self._line_edit.text() + self._text)


class Equals(Button):

    def __init__(self, widget: QWidget, line_edit: QLineEdit):
        super().__init__('=', line_edit)
        self._widget = widget

    def _on_click(self):
        try:
            self._line_edit.setText(str(eval(self._line_edit.text())))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Ошибка ввода.")
            msg.setWindowTitle("Атас")
            msg.exec()


class Calculator(QWidget):
    __buttons_list = ['7', '8', '9', '*',
                      '4', '5', '6', '-',
                      '1', '2', '3', '+']

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        formula_edit = QLineEdit()
        formula_edit.setReadOnly(True)
        grid.setSpacing(10)
        grid.addWidget(formula_edit, 0, 0, 1, 3)
        grid.addWidget(DelButton(formula_edit), 0, 3, 1, 1)
        grid.addWidget(ClearButton(formula_edit), 1, 0, 1, 1)
        grid.addWidget(CalculateButton('(', formula_edit), 1, 1, 1, 1)
        grid.addWidget(CalculateButton(')', formula_edit), 1, 2, 1, 1)
        grid.addWidget(CalculateButton('/', formula_edit), 1, 3, 1, 1)
        for b in self.__buttons_list:
            grid.addWidget(CalculateButton(b, formula_edit))
        grid.addWidget(CalculateButton('0', formula_edit), 5, 0, 1, 1)
        grid.addWidget(CalculateButton('.', formula_edit), 5, 1, 1, 1)
        grid.addWidget(Equals(self, formula_edit), 5, 2, 1, 2)
        self.setLayout(grid)
        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle('Calculator')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
