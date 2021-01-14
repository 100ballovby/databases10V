import sqlite3

conn = sqlite3.connect('test.db')
# в этой строчке создастся база данных с именем test.db
print('DB is opened!')

conn.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (1,'Zodiac',32,'Minsk',2000.00)
''')
"""Вставляем в таблицу COMPANY данные о работнике (заполняем все поля)"""
conn.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (2,'Ben',25,'California',15000.00)
''')
conn.commit()  # сохраняет изменения в таблице
conn.close()  # закрывает подключение к БД
