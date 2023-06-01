from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QWidget,
    QPushButton,
    QLineEdit,
    # layouts
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QFormLayout
)
import sys

# create an instance of QApplication
app = QApplication([])

# create your application GUI
window = QWidget()
window.setWindowTitle("Huffman")
window.setGeometry(100,100,280,80)

# create a label
# helloMsg = QLabel("<h1 style=\"color: red;\">hello world!</h1>", parent=window)
# helloMsg.move(60, 15)

"""
QLabel objects can display HTML-formatted text
"""

layout = QFormLayout()
layout.addRow("name: ", QLineEdit())

layout.addWidget(QPushButton("click me!"))
window.setLayout(layout)


# show your application's GUI
window.show()

# run your application's event loop
sys.exit(app.exec())