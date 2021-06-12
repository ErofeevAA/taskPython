import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QCheckBox, QPushButton, QSpinBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap


class Product:

    def __init__(self, name: str, image: str):
        self._number = 0
        self._name = name
        self._image = "assets/" + image

    def set_num(self, num):
        self._number = num

    @property
    def num(self):
        return self._number

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image


class Block:

    def __init__(self, product: Product, wid: QWidget):
        self._product = product

        self._is_checked = False
        self._checkbox = QCheckBox()
        self._checkbox.setChecked(False)
        self._checkbox.clicked.connect(self._checked)

        self._label = QLabel()
        self._label.setText(product.name)

        self._pixmap = QPixmap(product.image)
        self._image = QLabel(wid)
        self._image.setPixmap(self._pixmap.scaledToWidth(100))

        self._spinbox = QSpinBox()
        self._spinbox.setMaximum(10)
        self._spinbox.setMinimum(1)
        self._spinbox.setEnabled(False)
        self._spinbox.valueChanged.connect(self.set_num)

        self._dish = QVBoxLayout()
        self._dish.addWidget(self._image)
        self._dish.addWidget(self._label)

        self._layout = QHBoxLayout()
        self._layout.addLayout(self._dish)
        self._layout.addWidget(self._checkbox)
        self._layout.addWidget(self._spinbox)

    def _checked(self):
        self._is_checked = not self._is_checked
        self._spinbox.setEnabled(self._is_checked)
        num = self._spinbox.value() if self._is_checked else 0
        self._product.set_num(num)

    def set_num(self):
        self._product.set_num(self._spinbox.value())

    @property
    def product(self):
        return self._product

    @property
    def layout(self):
        return self._layout


class Cheque(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 650)
        self.setWindowTitle('Cheque')

        layout = QVBoxLayout()

        products = self._get_products()
        self._blocks = []
        for product in products:
            b = Block(product, self)
            layout.addLayout(b.layout)
            self._blocks.append(b)

        self._btn = QPushButton("Печать")
        self._btn.clicked.connect(self.print)
        layout.addWidget(self._btn)

        self.setLayout(layout)

    def print(self):
        cheque_layout = QGridLayout()
        cheque_layout.setHorizontalSpacing(100)

        msg = QMessageBox()
        msg.setWindowTitle("Чек")

        is_empty = True
        i = 0
        for block in self._blocks:
            p = block.product
            if p.num != 0:
                is_empty = False
                cheque_layout.addWidget(QLabel(p.name), i, 0)
                cheque_layout.addWidget(QLabel(str(p.num)), i, 1)
                i += 1
        if is_empty:
            msg.setText("Пустой заказ")
            msg.exec()
            return
        msg_layout = msg.layout()
        w = QWidget()
        w.setLayout(cheque_layout)
        msg_layout.addWidget(w)
        msg.exec()

    def _get_products(self):
        res = []
        with (open("assets/list.txt", "r")) as file:
            s = int(file.readline())
            self._sum = s
            for i in range(s - 1):
                name = file.readline()[:-1]
                res.append(Product(name, file.readline()[:-1]))
            name = file.readline()[:-1]
            res.append(Product(name, file.readline()))
            file.close()
        return res


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Cheque()
    widget.show()
    sys.exit(app.exec())
