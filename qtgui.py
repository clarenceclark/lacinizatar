#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon

import sys
REPLACEMENTS = (
    ('ль', 'l'),
    ('лі', 'lі'),
    ('ле', 'le'),
    ('лё', 'lo'),
    ('лю', 'lu'),
    ('ля', 'la'),
    ('Ль', 'L'),
    ('Ле', 'Le'),
    ('Лё', 'Lo'),
    ('Лю', 'Lu'),
    ('Ля', 'La'),
    ('зь', 'ź'),
    ('Зь', 'Ź'),
    ('нь', 'ń'),
    ('Нь', 'Ń'),
    ('сь', 'ś'),
    ('Сь', 'Ś'),
    ('ць', 'ć'),
    ('Ць', 'Ć'),
    ('а', 'a'),
    ('б', 'b'),
    ('в', 'v'),
    ('г', 'h'),
    ('ґ', 'g'),
    ('д', 'd'),
    ('е', 'je'),
    ('ё', 'jo'),
    ('ж', 'ž'),
    ('з', 'z'),
    ('і', 'i'),
    ('й', 'j'),
    ('к', 'k'),
    ('л', 'ł'),
    ('м', 'm'),
    ('н', 'n'),
    ('о', 'o'),
    ('п', 'p'),
    ('р', 'r'),
    ('с', 's'),
    ('т', 't'),
    ('у', 'u'),
    ('ў', 'ŭ'),
    ('ф', 'f'),
    ('х', 'ch'),
    ('ц', 'c'),
    ('ч', 'č'),
    ('ш', 'š'),
    ('ы', 'y'),
    ('э', 'e'),
    ('ю', 'ju'),
    ('я', 'ja'),
    ('А', 'A'),
    ('Б', 'B'),
    ('В', 'V'),
    ('Г', 'H'),
    ('Ґ', 'G'),
    ('Д', 'D'),
    ('Е', 'Je'),
    ('Ё', 'JO'),
    ('Ж', 'Ž'),
    ('З', 'Z'),
    ('І', 'I'),
    ('Й', 'J'),
    ('К', 'K'),
    ('Л', 'Ł'),
    ('М', 'M'),
    ('Н', 'N'),
    ('О', 'O'),
    ('П', 'P'),
    ('Р', 'R'),
    ('С', 'S'),
    ('Т', 'T'),
    ('У', 'U'),
    ('Ў', 'Ŭ'),
    ('Ф', 'F'),
    ('Х', 'Ch'),
    ('Ц', 'C'),
    ('Ч', 'Č'),
    ('Ш', 'Š'),
    ('Ы', 'Y'),
    ('Э', 'E'),
    ('Ю', 'Ju'),
    ('Я', 'Ja'),
    ('\'', ''),
)
J_REPLACMENTS = (
    ('je', 'ie'),
    ('jo', 'io'),
    ('ju', 'iu'),
    ('ja', 'ia'),
)
J_PREFIXES = 'bcčdfghjkłmnprsštvzžBCČDFGHJKŁMNPRSŠTVZŽ'


def lacin(name):
    if not name:
        return name
    for o, r in REPLACEMENTS:
        name = name.replace(o, r)
    for o, r in J_REPLACMENTS:
        for prefix in J_PREFIXES:
            name = name.replace(prefix + o, prefix + r)
    return name
class TextEditLacinizatar(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)
                self.setWindowTitle("Lacinizatar")
                self.setGeometry(300, 300, 500, 400)
                self.textEdit = QTextEdit()
                self.setIcon()
                self.btnPress1 = QPushButton("Clean")
                self.btnPress2 = QPushButton("Лацінізіраваць")

                layout = QVBoxLayout()
                layout.addWidget(self.textEdit)
                layout.addWidget(self.btnPress2)
                layout.addWidget(self.btnPress1)
                self.setLayout(layout)

                self.btnPress1.clicked.connect(self.btnPress1_Clicked)
                self.btnPress2.clicked.connect(self.btnPress2_Clicked)

        def setIcon(self):
                appIcon = QIcon("logo.png")
                self.setWindowIcon(appIcon)

        def btnPress1_Clicked(self):
                self.textEdit.clear()

        def btnPress2_Clicked(self):
                

                textboxValue = self.textEdit.toPlainText()
                yo = lacin(textboxValue)
                #self.clear()
                self.textEdit.clear()
                self.textEdit.setHtml("<font color='black' size='6'><black>"+ yo +"\n</font>")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditLacinizatar()
        win.show()
        sys.exit(app.exec_())
