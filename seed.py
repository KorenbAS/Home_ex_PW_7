import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Student, Group, Teacher, Subject, Grade


# Ініціалізація Faker
fake = Faker('uk-Ua')

# Генерація даних

# Створення функції для генерації випадкових даних та вставки їх у таблицю
def insert_fake_data(model, num_entries, **kwargs):
    for _ in range(num_entries):
        fake_data = model.fake(**kwargs) if hasattr(model, 'fake') else {}
        entry = model(**fake_data)
        session.add(entry)


# Збереження змін та закриття сесії
if __name__ == '__main__':
    try:
        insert_fake_data(Group, 3)
        insert_fake_data(Teacher, 5)

        groups = session.query(Group).all()
        insert_fake_data(Student, 50, group=random.choice(groups))

        teachers = session.query(Teacher).all()
        insert_fake_data(Subject, 8, Teacher=random.choice(teachers))

        students = session.query(Student).all()
        subjects = session.query(Subject).all()
        for student in students:
            for subject in subjects:
                num_grades = random.randint(1, 20)
                insert_fake_data(Grade, num_grades, student=student, subject=subject)

        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()







