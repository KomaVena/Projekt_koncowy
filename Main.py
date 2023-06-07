import sys
import os
import xmltodict
import json
import yaml
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox

class DataConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Data Converter")
        self.layout = QVBoxLayout()
        self.source_file_label = QLabel("Source File:")
        self.source_file_edit = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.target_file_label = QLabel("Target File:")
        self.target_file_edit = QLineEdit()
        self.convert_button = QPushButton("Convert")

        self.browse_button.clicked.connect(self.browse_source_file)
        self.convert_button.clicked.connect(self.convert_data)

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.source_file_label)
        file_layout.addWidget(self.source_file_edit)
        file_layout.addWidget(self.browse_button)

        self.layout.addLayout(file_layout)
        self.layout.addWidget(self.target_file_label)
        self.layout.addWidget(self.target_file_edit)
        self.layout.addWidget(self.convert_button)

        self.setLayout(self.layout)

    def browse_source_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_path, _ = file_dialog.getOpenFileName(self, "Select Source File")
        self.source_file_edit.setText(file_path)

    def convert_data(self):
        source_file_path = self.source_file_edit.text()
        target_file_path = self.target_file_edit.text()

        if not os.path.exists(source_file_path):
            QMessageBox.warning(self, "Error", "Source file does not exist.")
            return

        file_extension = os.path.splitext(source_file_path)[1][1:]
        if file_extension not in ["xml", "json", "yml", "yaml"]:
            QMessageBox.warning(self, "Error", "Unsupported file format.")
            return

        try:
            with open(source_file_path, "r") as source_file:
                data = source_file.read()

            if file_extension == "xml":
                converted_data = xmltodict.parse(data)
            elif file_extension == "json":
                converted_data = json.loads(data)
            else:
                converted_data = yaml.safe_load(data)

            target_extension = os.path.splitext(target_file_path)[1][1:]
            if target_extension == "xml":
                converted_data = xmltodict.unparse(converted_data, pretty=True)
            elif target_extension == "json":
                converted_data = json.dumps(converted_data, indent=4)
            else:
                converted_data = yaml.dump(converted_data, default_flow_style=False)

            with open(target_file_path, "w") as target_file:
                target_file.write(converted_data)

            QMessageBox.information(self, "Success", "Conversion successful.")

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = DataConverter()
    converter.show()
    sys.exit(app.exec_())
