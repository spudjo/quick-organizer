import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout
import python_organizer


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Python Organizer")
        self.setFixedSize(600, 400)
        self.input = QLineEdit("Enter path...")
        self.output = QLineEdit("Enter path...")
        self.button = QPushButton("Organize")
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.output)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(lambda: self.call_organizer(self.input.text(), self.output.text()))

    def call_organizer(self, input, output):
        python_organizer.organize(input, output)
        # print(input)
        # print(output)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
