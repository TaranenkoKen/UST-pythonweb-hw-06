import random
from datetime import date
from faker import Faker
from database import SessionLocal
from models import Group, Teacher, Subject, Student, Grade

fake = Faker("uk_UA")

GROUPS_COUNT = 3
TEACHERS_COUNT = random.randint(3, 5)
SUBJECTS_COUNT = random.randint(5, 8)
STUDENTS_COUNT = random.randint(30, 50)
MIN_GRADES_PER_STUDENT = 10
MAX_GRADES_PER_STUDENT = 20

SUBJECT_NAMES = [
    "Математичний аналіз",
    "Лінійна алгебра",
    "Фізика",
    "Програмування",
    "Бази даних",
    "Операційні системи",
    "Алгоритми та структури даних",
    "Дискретна математика",
]


def seed():
    session = SessionLocal()
    try:
        groups = []
        for i in range(1, GROUPS_COUNT + 1):
           group = Group(name=f"{fake.bothify(text='??-##')}")
           session.add(group)
           groups.append(group)
        session.flush()

        teachers = []
        for _ in range(TEACHERS_COUNT):
            teacher = Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )
            session.add(teacher)
            teachers.append(teacher)
        session.flush()

        subjects = []
        chosen_names = random.sample(SUBJECT_NAMES, SUBJECTS_COUNT)
        for name in chosen_names:
            subject = Subject(
                name=name,
                teacher_id=random.choice(teachers).id,
            )
            session.add(subject)
            subjects.append(subject)
        session.flush()

        students = []
        for _ in range(STUDENTS_COUNT):
            student = Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                group_id=random.choice(groups).id,
            )
            session.add(student)
            students.append(student)
        session.flush()

        for student in students:
            num_grades = random.randint(MIN_GRADES_PER_STUDENT, MAX_GRADES_PER_STUDENT)
            for _ in range(num_grades):
                subject = random.choice(subjects)
                grade_value = random.randint(60, 100)
                received = fake.date_between(start_date=date(2025, 10, 1), end_date='today')
                grade = Grade(
                    student_id=student.id,
                    subject_id=subject.id,
                    grade=grade_value,
                    date_received=received,
                )
                session.add(grade)

        session.commit()
        print("✅ База даних успішно заповнена!")
        print(f"Групи: {GROUPS_COUNT}")
        print(f"Викладачі: {TEACHERS_COUNT}")
        print(f"Предмети: {SUBJECTS_COUNT}")
        print(f"Студенти: {STUDENTS_COUNT}")
    except Exception as e:
        session.rollback()
        print(f"❌ Помилка: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed()