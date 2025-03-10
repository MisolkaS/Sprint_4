import random
from datetime import datetime, timedelta

def get_test_data():
    return [
        {
            "name": "Алина",
            "lastname": "Ситалова",
            "address": "Улица Планерная, 1",
            "metro": "Черкизовская",
            "phone": "79312312311",
            "date": None,
            "period": "сутки",
            "color": ["grey", "black"],
            "comment": "Позвоните в домофон",
            "button": "top"
        },
        {
            "name": "София",
            "lastname": "Прекрасная",
            "address": "Улица Пушкина, 2",
            "metro": "Арбатская",
            "phone": "89312312311",
            "date": None,
            "period": "пятеро суток",
            "color": ["grey"],
            "comment": "Позвоните за час",
            "button": "bottom"
        }
    ]


def get_random_date():
    start_date = datetime.now() + timedelta(days=1)
    end_date = start_date + timedelta(days=7)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%d.%m.%Y")