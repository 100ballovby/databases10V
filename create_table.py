import sqlite3

conn = sqlite3.connect('test.db')
# в этой строчке создастся база данных с именем test.db
print('DB is opened!')

conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);
''')  # создаем таблицу с данными о работниках компании
print('Table created')
conn.close()  # закрывает подключение к БД

