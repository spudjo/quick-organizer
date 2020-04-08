import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QTextEdit, QPushButton, QVBoxLayout
import python_organizer


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Python Organizer")
        self.setFixedSize(600, 400)
        self.input = QLineEdit("")
        self.button_add = QPushButton("Add to list")
        self.input_list = QTextEdit()
        self.input_list.setEnabled(False)
        self.output = QLineEdit("")
        self.button_submit = QPushButton("Organize")
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button_add)
        layout.addWidget(self.input_list)
        layout.addWidget(self.output)
        layout.addWidget(self.button_submit)
        self.setLayout(layout)
        self.button_add.clicked.connect(self.add_text)
        self.button_submit.clicked.connect(self.call_organizer)

    def add_text(self):
        self.input_list.insertPlainText("{}\n".format(self.input.text()))
        self.input.setText("")

    def call_organizer(self):

        l = self.input_list.document().toPlainText().split('\n')
        python_organizer.organize(l, self.output.text())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
