from aqt import gui_hooks
from typing import Callable
from aqt.editor import Editor
from . import gui


def editor_button(buttons: list[str], editor: Editor) -> None:
    button = editor.addButton("plus.png", "Add list", add_list_clicked())
    buttons.append(button)


def add_list_clicked() -> Callable[[Editor], None]:
    def launch(editor: Editor) -> None:
        list_input = gui.ListInput(editor)
        list_input.exec()
    return launch


gui_hooks.editor_did_init_buttons.append(editor_button)
