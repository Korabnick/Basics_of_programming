from datetime import date
from datetime import timedelta

def captain_notes(notes, date):
    oDay = timedelta(days=1)
    diary = open('notes.txt', 'w')
    for note in notes:
        diary.write(str(date)+ ': ' + note + '\n')
        date = date + oDay
    diary.close()
captain_notes(['Сегодня весь день был штиль и пришлось использовать весла.', 
'Море разбушевалось, но все еще было частично спокойным, паруса справлялись со своей задачей.', 
'Мы наткнулись на остров, которого нет на картах, после нескольких минут пребывания на острове стало понятно, что здесь очень опас...'], 
date(2022, 10, 15))