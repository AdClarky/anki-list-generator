from aqt.editor import Editor
from aqt.qt import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from aqt import mw


def convert_to_list(data: list[str]) -> list[str]:
    length = len(data)
    data_list: list[str] = [f"1. {{{{c1::{data[0]}}}}}<br>" + "".join([f"{j + 2}.<br>" for j in range(length - 1)])]
    for i in range(length):
        if i == 0:
            continue
        card = ""
        for j in range(length):
            if j == i-1:
                card += f"{j + 1}. {data[i-1]}<br>"
            elif j == i:
                card += f"{j + 1}. {{{{c1::{data[i]}}}}}<br>"
            else:
                card += f"{j + 1}.<br>"
        data_list.append(card)
    return data_list


class ListInput(QDialog):
    def __init__(self, editor: Editor):
        super().__init__(mw)

        self.editor = editor
        self.setWindowTitle("Values to List")
        self.setGeometry(100, 100, 300, 200)

        self.inputLabels: list[QLabel] = []
        self.inputFields: list[QLineEdit] = []

        for i in range(3):
            self.inputLabels.append(QLabel(f"Entry {i + 1}:"))
            self.inputFields.append(QLineEdit(self))

        self.more_button = QPushButton("Add row", self)
        self.ok_button = QPushButton("OK", self)
        self.cancel_button = QPushButton("Cancel", self)

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.more_button)

        self.field_layout = QVBoxLayout()
        for label, field in zip(self.inputLabels, self.inputFields):
            self.field_layout.addWidget(label)
            self.field_layout.addWidget(field)
        main_layout.addLayout(self.field_layout)

        main_layout.addWidget(self.ok_button)
        main_layout.addWidget(self.cancel_button)

        self.setLayout(main_layout)

        self.more_button.clicked.connect(self.more_clicked)
        self.ok_button.clicked.connect(self.ok_clicked)
        self.cancel_button.clicked.connect(self.reject)

    def accumulate_data(self) -> list[str]:
        data = [field.text() for field in self.inputFields]
        return data

    def more_clicked(self):
        self.inputLabels.append(QLabel(f"Entry {len(self.inputFields) + 1}:"))
        self.field_layout.addWidget(self.inputLabels[-1])
        self.inputFields.append(QLineEdit(self))
        self.field_layout.addWidget(self.inputFields[-1])

    def ok_clicked(self):
        data = self.accumulate_data()
        cards = convert_to_list(data)
        self.add_cloze(cards)

    def add_cloze(self, cards: list[str]) -> None:
        model = mw.col.models.by_name("_Cloze")
        for card in cards:
            new_note = mw.col.new_note(model)
            new_note["Text"] = card
            deck = mw.col.decks.id_for_name("Test")
            mw.col.add_note(new_note, deck)
