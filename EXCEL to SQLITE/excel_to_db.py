import sqlite3
import pandas as pd

con = sqlite3.connect('my_music.db')
# подключаемся к БД my_music
wb = pd.read_excel('music.xlsx', sheet_name=None)


