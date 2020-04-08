import sys
from PySide2.QtWidgets import QApplication, QDialog, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, QMessageBox
import file_organizer


def create_popup(text='Text', informative_text='Informative Text', window_title='Title', icon=QMessageBox.Information):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setText(text)
    msg.setFixedWidth(1000)
    msg.setInformativeText(informative_text)
    msg.setWindowTitle(window_title)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle('Quick Organizer')
        self.setFixedSize(600, 400)

        self.input_label = QLabel('Input Folders')
        self.input_button = QPushButton('Select Input Folder')
        self.input_button.setFixedSize(125, 25)
        self.input_button.clicked.connect(self.get_input)

        self.input_list = QTextEdit()
        self.input_list.setReadOnly(True)

        self.output_label = QLabel('Output Folder')
        self.output_field = QTextEdit('')
        self.output_field.setFixedHeight(25)
        self.output_field.setReadOnly(True)
        self.output_button = QPushButton('Select Output Folder')
        self.output_button.setFixedSize(125, 25)
        self.output_button.clicked.connect(self.get_output)

        self.button_submit = QPushButton('Organize')
        self.button_submit.clicked.connect(self.call_organizer)

        self.file_browser = QFileDialog()

        self.layout_main = QVBoxLayout()
        self.layout_row_a = QHBoxLayout()
        self.layout_row_b = QHBoxLayout()
        self.layout_row_c = QHBoxLayout()

        self.layout_main.addLayout(self.layout_row_a)
        self.layout_main.addLayout(self.layout_row_b)
        self.layout_main.addLayout(self.layout_row_c)
        self.layout_main.addWidget(self.button_submit)

        self.layout_row_a.addWidget(self.input_label)
        self.layout_row_a.addWidget(self.input_button)

        self.layout_row_b.addWidget(self.input_list)

        self.layout_row_c.addWidget(self.output_label)
        self.layout_row_c.addWidget(self.output_field)
        self.layout_row_c.addWidget(self.output_button)

        self.setLayout(self.layout_main)

    def get_input(self):

        directory = QFileDialog.getExistingDirectory(self)
        if directory is not '':
            self.input_list.insertPlainText("{}\n".format(directory))
            self.input_list.verticalScrollBar().setValue(self.input_list.verticalScrollBar().maximum())

    def get_output(self):

        directory = QFileDialog.getExistingDirectory(self)
        if directory is not '':
            self.output_field.setText(directory)

    def call_organizer(self):

        full_input = self.input_list.document().toPlainText().split('\n')
        output = self.output_field.toPlainText()

        if len(full_input) > 1 and output is not '':

            print(full_input[:-1])
            print(output)
            file_organizer.organize(full_input[:-1], output)

            create_popup(text='Success!', informative_text='All files have been sorted', window_title='Success!', icon=QMessageBox.Information)

        elif len(full_input) == 1 and output is '':

            create_popup(text='No input or output found', informative_text='Please select input and output directories', window_title='Error', icon=QMessageBox.Critical)

        elif len(full_input) == 1:

            create_popup(text='No input found', informative_text='Please select at least 1 input directory', window_title='Error', icon=QMessageBox.Critical)

        elif output is '':

            create_popup(text='No output found', informative_text='Please select an output directory', window_title='Error', icon=QMessageBox.Critical)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
