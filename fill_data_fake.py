from datetime import datetime, date, timedelta
from faker import Faker
from random import randint
import sqlite3


DISCIPLINES = [
    "Высшая математика",
    "История Украины",
    "Философия",
    "Английский язык",
    "Программирование",
    "Физкультура",
    "Дифференциальная геометрия"
]

GROUPS = ["МТБ-08", "ДГБ-099", "ТПК404"]
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50

fake = Faker("uk-UA")
connect = sqlite3.connect('studies.db')
cur = connect.cursor()

def fill_teachers(number_teachers):
    teachers = [fake.name() for _ in range(number_teachers)]
    sql = "INSERT INTO teachers(fullname) VALUES(?);"
    cur.executemany(sql, zip(teachers,))


def fill_disciplines(disciplines, number_teachers):
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);"
    cur.executemany(sql, zip(disciplines, iter(randint(1, number_teachers) for _ in range(len(disciplines)))))

def fill_groups(groups):
    sql = "INSERT INTO groups(name) VALUES(?);"
    cur.executemany(sql, zip(groups, ))
    
def fill_students(number_students):
    students = [fake.name() for _ in range(number_students)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(GROUPS)) for _ in range(number_students))))
    
def fill_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-20", "%Y-%m-%d")
    sql = "INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?);"
    
    def get_list_date(start: date, end: date):
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result
    
    list_dates = get_list_date(start_date, end_date)
    
    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(DISCIPLINES))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(6)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1,5), day.date()))
    cur.executemany(sql, grades)
 
def main():
    try:
        fill_teachers(NUMBER_TEACHERS)
        fill_disciplines(DISCIPLINES, NUMBER_TEACHERS)
        fill_students(NUMBER_STUDENTS)
        fill_groups(GROUPS)
        fill_grades()
        connect.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        connect.close()
      

if __name__ == "__main__":
    main()
    
    