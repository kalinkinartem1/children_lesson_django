import os
import django
from faker import Faker
import random

import datetime
# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "children.settings")
django.setup()

# После этого вы можете импортировать модели
from app.models import *

# удаление всех объектов
Record.objects.all().delete()
Schedule.objects.all().delete()
Lesson.objects.all().delete()
Child.objects.all().delete()

# Ваш код для генерации данных
fake = Faker('ru_RU')


lesson_data = [
    {"name": "Футбольный кружок", "description": "Учимся играть в футбол", "teacher_name": "Иван Иванов"},
    {"name": "Художественная мастерская", "description": "Творческие занятия", "teacher_name": "Мария Петрова"},
    {"name": "Робототехника", "description": "Создаем своих роботов", "teacher_name": "Алексей Сидоров"},
    {"name": "Танцевальная студия", "description": "Обучение различным танцевальным стилям", "teacher_name": "Екатерина Николаева"},
    {"name": "Шахматный кружок", "description": "Изучаем стратегии в шахматах", "teacher_name": "Павел Сергеев"},
    {"name": "Кулинарная мастерская", "description": "Готовим вкусные блюда", "teacher_name": "Ольга Куликова"},
    {"name": "Биологический кружок", "description": "Изучение живой природы", "teacher_name": "Андрей Васильев"},
    {"name": "Музыкальный оркестр", "description": "Игра на музыкальных инструментах", "teacher_name": "Наталья Смирнова"},
    {"name": "Химический кружок", "description": "Эксперименты с химическими веществами", "teacher_name": "Владимир Лебедев"},
    {"name": "Литературный клуб", "description": "Обсуждение литературных произведений", "teacher_name": "Татьяна Иванова"},
    {"name": "Искусство актерской игры", "description": "Обучение актерскому мастерству", "teacher_name": "Дмитрий Козлов"},
    {"name": "Компьютерная графика", "description": "Изучение программ для создания графики", "teacher_name": "Елена Морозова"},
    {"name": "Астрономический кружок", "description": "Наблюдение за звездами и планетами", "teacher_name": "Сергей Галкин"},
    {"name": "Живопись", "description": "Обучение технике живописи", "teacher_name": "Анастасия Белова"},
    {"name": "Физический эксперимент", "description": "Изучение законов физики через эксперименты", "teacher_name": "Игорь Соколов"},
    {"name": "Французский язык", "description": "Изучение французского языка", "teacher_name": "София Дюран"},
    {"name": "Юный геолог", "description": "Изучение геологии и минералов", "teacher_name": "Артем Ковалев"},
    {"name": "Театральная студия", "description": "Обучение театральному мастерству", "teacher_name": "Алиса Горбачева"},
    {"name": "Каратэ", "description": "Тренировки по каратэ", "teacher_name": "Денис Яковлев"},
]

# Добавляем каждый элемент данных в базу данных
from tqdm import tqdm


# Добавляем каждый элемент данных в базу данных
# ...

# Добавляем каждый элемент данных в базу данных
lessons = []
for lesson_info in tqdm(lesson_data, desc="Creating Lessons"):
    lesson = Lesson.objects.create(**lesson_info)
    lessons.append(lesson)

from tqdm import tqdm

# ...

# Добавляем каждый элемент данных в базу данных
lessons = []
for lesson_info in tqdm(lesson_data, desc="Creating Lessons"):
    lesson = Lesson.objects.create(**lesson_info)
    lessons.append(lesson)

from tqdm import tqdm

for lesson in tqdm(lessons, desc="Creating Schedules"):
    for _ in range(4):  # 4 типа времени
        for day in range(4):  # 4 даты
            date = datetime.datetime.now() + datetime.timedelta(days=day)
            time = fake.time()
            schedule = Schedule.objects.create(kids_circle=lesson, date=date, time=time)

            # Генерируем записи для каждого расписания
            num_records = random.randint(5, 20)
            for _ in tqdm(range(num_records), desc="Creating Records", leave=False):
                # Создаем нового ребенка или выбираем существующего, если он уже записан
                existing_child = Child.objects.filter(records__schedule=schedule).first()
                if existing_child is None or Record.objects.filter(schedule=schedule, child=existing_child).exists():
                    child = Child.objects.create(
                        last_name=fake.last_name(),
                        first_name=fake.first_name(),
                        patronymic=fake.middle_name(),
                        birth_date=fake.date_of_birth(minimum_age=4, maximum_age=18)
                    )
                else:
                    child = existing_child

                # Проверяем, записан ли ребенок на текущее расписание
                if not Record.objects.filter(schedule=schedule, child=child).exists():
                    Record.objects.create(schedule=schedule, child=child)



