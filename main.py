from sqlalchemy import func, desc

from conf.db import session
from conf.models import Student, Group, Teacher, Subject, Grade


def select_1():
    return session.query(Student.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                  .select_from(Grade).join(Student).group_by(Student.id) \
                  .order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    return session.query(Student.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                  .select_from(Grade).join(Student).join(Subject).filter(Subject.name == subject_name) \
                  .group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()

def select_3(subject_name):
    return session.query(Group.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                  .select_from(Grade).join(Student).join(Group).join(Subject).filter(Subject.name == subject_name) \
                  .group_by(Group.id).all()

def select_4():
    return session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')).all()

def select_5(teacher_name):
    return session.query(Subject.name).select_from(Teacher).join(Subject) \
                  .filter(Teacher.name == teacher_name).all()

def select_6(group_name):
    return session.query(Student.name).select_from(Group).join(Student) \
                  .filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    return session.query(Student.name, Grade.value).select_from(Group).join(Student).join(Grade).join(Subject) \
                  .filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(teacher_name):
    return session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                  .select_from(Teacher).join(Subject).join(Grade).filter(Teacher.name == teacher_name) \
                  .group_by(Teacher.id).all()

def select_9(student_name):
    return session.query(Subject.name).select_from(Student).join(Grade).join(Subject) \
                  .filter(Student.name == student_name).all()

def select_10(student_name, teacher_name):
    return session.query(Subject.name).select_from(Student).join(Grade).join(Subject).join(Teacher) \
                  .filter(Student.name == student_name, Teacher.name == teacher_name).all()

# Виклик функцій
result_1 = select_1()
result_2 = select_2('Subject 1')
result_3 = select_3('Subject 1')
result_4 = select_4()
result_5 = select_5('Teacher 1')
result_6 = select_6('Group 1')
result_7 = select_7('Group 1', 'Subject 1')
result_8 = select_8('Teacher 1')
result_9 = select_9('Student 1')
result_10 = select_10('Student 1', 'Teacher 1')

# Виведення результатів
print("Result 1:", result_1)
print("Result 2:", result_2)
print("Result 3:", result_3)
print("Result 4:", result_4)
print("Result 5:", result_5)
print("Result 6:", result_6)
print("Result 7:", result_7)
print("Result 8:", result_8)
print("Result 9:", result_9)
print("Result 10:", result_10)

# Закриття сесії
session.close()
