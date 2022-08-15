"""
Задача на структуры данных

У аналитика большое количество задач, которые держать в голове невозможно. Задачу можно описать так:
- Что необходимо сделать
- С кем поделиться результатами
- Статус задачи
- Дата, когда задача пришла (нельзя же неделями игнорировать просителя! ;) )
Принята ли завершенная задача заказчиком (или он вернется с просьбой доделать)
Какая структура данных для хранения таких задач здесь уместна и почему?
Любые численные и др аргументы и сравнения приветствуются. Выполните простую реализацию.

"""

import datetime
import pandas as pd
from IPython.display import display

"""Здесь хорошо подойдет такая структура как:
Map
Map — это структура, которая хранит данные в парах ключ/значение, где каждый ключ уникален.
Иногда её также называют ассоциативным массивом или словарём.
Map часто используют для быстрого поиска данных.
"""

tasks = {
    "task description": "сделать модель",
    "target person": "Stanislav Kachnov",
    "task status": "Open",
    "task start date ": datetime.datetime.now()
}

"""
Ещё хорошо бы добавить поле id, чтобы у задачи был исполнитель
"""

tasks['id'] = 0

"""
При помощи pandas можно удобно сформировать таблицу для хранения и визуализации информации
"""

df = pd.DataFrame(tasks, index=[0])
display(df)