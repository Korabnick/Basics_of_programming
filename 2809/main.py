from datetime import date
from datetime import timedelta

def captain_notes(notes, date):
    oDay = timedelta(days=1)
    f = open('notes.txt', 'w')
    for note in notes:
        f.write(str(date)+ ': ' + note + '\n')
        date = date + oDay
    f.close()
captain_notes(['Сегодня весь день был штиль и пришлось использовать весла.', 'Море разбушевалось, но все еще было частично спокойным, паруса справлялись со своей задачей.', 
'Мы наткнулись на остров, которого нет на картах'], 
date(2022, 10, 15))