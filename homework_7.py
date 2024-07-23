import sqlite3 as sql

with sql.connect('student.db') as conn:
    cursor = conn.cursor()
    # cursor.execute(''' DROP TABLE IF EXISTS student''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby TEXT,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    age DATE DEFAULT 18,
    grades INTEGER DEFAULT 0
    )''')

    cursor.execute('''INSERT INTO student (hobby, name, surname, age, grades)
    VALUES
    ('gym', 'timur', 'chikeev', 20, 60),
    ('reading', 'aidar', 'akmataliev', 22, 80),
    ('playing guitar', 'sultan', 'asheraliev', 23, 1),
    ('anime', 'aman', 'osmonaliev', 21, 18),
    ('cooking', 'bekter', 'ghoul', 24, 0),
    ('dota', 'rudolf', 'machmatimovan', 37, 5),
    ('3d', 'aldiyar', 'chumbawamba', 29, 78),
    ('games', 'komet', 'ahumbaev', 25, 100),
    ('clubbing', 'telegay', 'ashimova', 35, 4),
    ('nails', 'katya', 'barg', 15, 67)
    
    ''')

    cursor.execute('''DELETE FROM student WHERE id>10''')

    #Вывожу всех у кого фамилия больше 10 символов
    cursor.execute('''SELECT id, hobby, name, surname, length(surname), age, grades FROM student WHERE length(surname) > 10''')
    for i in cursor.fetchall():
        print(i)

    # Обновляю имена всех студентов у которых больше 10ти балов
    cursor.execute('''UPDATE student SET name="genius" WHERE grades > 10''')
    cursor.execute('''SELECT * FROM student ''')
    for i in cursor.fetchall():
        print(i)

    # Удаляю всех студентов с четным айди
    cursor.execute('''DELETE FROM student WHERE id % 2 == 0 ''')
