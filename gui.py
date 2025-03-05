from aqt.editor import Editor
from aqt.qt import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout


class ListInput(QDialog):
    def __init__(self, editor: Editor):
        super().__init__()

        self.editor = editor
        self.setWindowTitle("Values to List")
        self.setGeometry(100, 100, 300, 200)

        # Labels and Input Fields
        self.label1 = QLabel("Enter first string:")
        self.input1 = QLineEdit(self)

        self.label2 = QLabel("Enter second string:")
        self.input2 = QLineEdit(self)

        self.label3 = QLabel("Enter third string:")
        self.input3 = QLineEdit(self)

        # Buttons
        self.ok_button = QPushButton("OK", self)
        self.cancel_button = QPushButton("Cancel", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.label3)
        layout.addWidget(self.input3)
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        # Button Connections
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
