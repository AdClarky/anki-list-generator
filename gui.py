from aqt.editor import Editor
from aqt.qt import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from aqt import mw


def convert_to_list(data: list[str]) -> list[str]:
    length = len(data)
    data_list: list[str] = [f"1. {{{{c1::{data[0]}}}}}\n" + "".join([f"{j + 2}.\n" for j in range(length - 1)])]
    for i in range(length):
        if i == 0:
            continue
        card = ""
        for j in range(length):
            if j == i-1:
                card += f"{j + 1}. {data[i-1]}\n"
            elif j == i:
                card += f"{j + 1}. {{{{c1::{data[i]}}}}}\n"
            else:
                card += f"{j + 1}.\n"
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
            self.inputLabels.append(QLabel(f"String {i + 1}:"))
            self.inputFields.append(QLineEdit(self))

        self.ok_button = QPushButton("OK", self)
        self.cancel_button = QPushButton("Cancel", self)

        layout = QVBoxLayout()
        for label, field in zip(self.inputLabels, self.inputFields):
            layout.addWidget(label)
            layout.addWidget(field)

        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        self.ok_button.clicked.connect(self.ok_clicked)
        self.cancel_button.clicked.connect(self.reject)

    def accumulate_data(self) -> list[str]:
        data = [field.text() for field in self.inputFields]
        return data

    def ok_clicked(self):
        data = self.accumulate_data()
        cards = convert_to_list(data)
        print(cards)

    def add_cloze(self, data: str) -> None:
        model = mw.col.models.by_name("_Cloze")
        new_note = mw.col.new_note(model)
        new_note["Text"] = data
        deck = mw.col.decks.id_for_name("Test")
        mw.col.add_note(new_note, deck)


if __name__ == '__main__':
    myList = convert_to_list(["One", "Two", "Three", "Four"])
    [print(item) for item in myList]
