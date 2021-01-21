import sqlite3

conn = sqlite3.connect('mydb.db')

conn.execute('''CREATE TABLE TEST
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL);
''')

conn.execute('''
INSERT INTO TEST (ID, NAME, AGE)
VALUES (1, 'George', 25);
''')
conn.execute('''
INSERT INTO TEST (ID, NAME, AGE)
VALUES (2, 'Nick', 32);
''')
conn.execute('''
INSERT INTO TEST (ID, NAME, AGE)
VALUES (3, 'Mike', 29);
''')
conn.execute('''
INSERT INTO TEST (ID, NAME, AGE)
VALUES (4, 'Harry', 22);
''')
conn.commit()


# вывести всю информацию из БД
cursor = conn.cursor()
# res = conn.execute('SELECT id, name, age FROM TEST')
cursor.execute('SELECT id, name, age FROM TEST')
rows = cursor.fetchall()
for row in rows:
    print(row)

#for row in res:
#    print('ID = ', row[0])
#    print('Name = ', row[1])
#    print('Age = ', row[2])

conn.close()