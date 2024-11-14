#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup, QLineEdit,  QTextEdit, QListWidget,  QInputDialog
import json

def show_note():
    name = list_field.selectedItems()[0].text()
    large_field.setText(notes[name]['текст'])
    list_field_2.clear()
    list_field_2.addItems(notes[name]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(win, 'Добавить заметку', 'Название заметки:')

    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        list_field.addItem(note_name)

def dell_note():
    if list_field.selectedItems():
        name = list_field.selectedItems()[0].text()
        del notes[name]
        list_field.clear()
        list_field_2.clear()
        large_field.clear()
        list_field.addItems(notes)

def save_note():
    if list_field.selectedItems():
        name = list_field.selectedItems()[0].text()
        text = large_field.toPlainText()
        notes[name]['текст'] = text

def add_tag():
    if list_field.selectedItems():
        key = list_field.selectedItems()[0].text()
        tag = field_teg.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_field_2.addItem(tag)
            field_teg.clear()
def del_tag():
    if list_field.selectedItems():
        zametka = list_field.selectedItems()[0].text()
        tag = list_field_2.selectedItems()[0].text()
        notes[zametka]['теги'].remove(tag)
        list_field_2.clear()
        list_field_2.addItems(notes[zametka]['теги'])

def search_tag():
    tags = field_teg.text() 
    if button_poisk.text() == 'Искать заметки по тегу' and tags:
        notes_filtred = {}
        for i in notes:
            if tags in notes[i]['теги']:
                notes_filtred[i] = notes[i]
        button_poisk.setText('Сбросить поиск')
        list_field.clear()
        list_field_2.clear()
        list_field.addItems(notes_filtred)
    elif button_poisk.text() == 'Сбросить поиск':
        field_teg.clear()
        list_field.clear()
        list_field_2.clear()
        list_field.addItems(notes)
        button_poisk.setText('Искать заметки по тегу')




with open('notes.json' , 'r', encoding = 'utf-8') as file:
    notes = json.load(file)

app = QApplication([])
win = QWidget()
list_field =  QListWidget()
list_field_2 = QListWidget()
large_field = QTextEdit()
field_teg = QLineEdit()
win.setWindowTitle('Умные заметки')
text_zametki = QLabel('Список заметок')
text_tegi = QLabel('Список тегов')
button_sozdanie = QPushButton('Создать заметку')
button_udalenie = QPushButton('Удалить заметку')
button_sokhranenie = QPushButton('Сохранить заметку')
button_dobavlenie = QPushButton('Добавить к заметкe')
button_otkreplenie = QPushButton('Открепление от заметки')
button_poisk = QPushButton('Искать заметки по тегу')
field_teg.setPlaceholderText('Введите тег...')


layout_gorizantal = QHBoxLayout()
layout_gorizantal.addWidget(button_sozdanie)
layout_gorizantal.addWidget(button_udalenie)

layout_goriz_2 = QHBoxLayout()
layout_goriz_2.addWidget(button_dobavlenie)
layout_goriz_2.addWidget(button_otkreplenie)



layout_vertical = QVBoxLayout()
layout_vertical.addWidget(text_zametki)
layout_vertical.addWidget(list_field)
layout_vertical.addLayout(layout_gorizantal)
layout_vertical.addWidget(button_sokhranenie)
layout_vertical.addWidget(text_tegi)
layout_vertical.addWidget(list_field_2)
layout_vertical.addWidget(field_teg)
layout_vertical.addLayout(layout_goriz_2)
layout_vertical.addWidget(button_poisk)

layout_important = QHBoxLayout()
layout_important.addWidget(large_field)   
layout_important.addLayout(layout_vertical)

win.setLayout(layout_important)

list_field.addItems(notes)
list_field.itemClicked.connect(show_note)
button_sozdanie.clicked.connect(add_note)
button_udalenie.clicked.connect(dell_note)
button_sokhranenie.clicked.connect(save_note)
button_dobavlenie.clicked.connect(add_tag)
button_otkreplenie.clicked.connect(del_tag)
button_poisk.clicked.connect(search_tag)







win.show()
app.exec_()

with open('notes.json', 'w', encoding = 'utf-8') as file:
    json.dump(notes, file)












