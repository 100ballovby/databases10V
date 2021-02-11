import sqlite3 as sql

conn = sql.connect('lesson.db')
choice = input('1 - добавить, 2 - получить: ')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS 'test' ('name' STRING, 'surname' STRING)")

    if choice == '1':
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        cur.execute(f"INSERT INTO 'test' VALUES ('{name}', '{surname}')")

    elif choice == '2':
        cur.execute("SELECT * FROM 'test'")
        rows = cur.fetchall()
        for i in rows:
            print(i[0], i[1])

    else:
        print('Такой опции нет.')

conn.commit()
conn.close()