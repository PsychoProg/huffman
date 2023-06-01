""" Dialog-style application """

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout
)

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Dialog")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()

        formLayout.addRow("name: ", QLineEdit())
        formLayout.addRow("age: ", QLineEdit())
        formLayout.addRow("gender: ", QLineEdit())

        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )

        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


if __name__ == '__main__': 
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())