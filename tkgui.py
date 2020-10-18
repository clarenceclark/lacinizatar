#!/usr/bin/env python
from tkinter import *
import tkinter as tk

root=Tk()
root.title('Lacinizatar') 
photo = PhotoImage(file = "logo.png")
root.iconphoto(False, photo)

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




def gui():
    

    inputValue=textBox.get("1.0","end-1c")
    textBox.delete('1.0', END)
    oj = lacin(inputValue)
    return oj
def output():
    
    textBox.insert(tk.END,gui())

textBox=Text(root, height=25, width=100)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Лацінізіраваць", 
                    command=lambda: output())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()
