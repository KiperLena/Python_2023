import os

from sqlalchemy import and_, or_, not_, desc, func, distinct, text

from zadanie39.database import DATABASE_NAME, Session
import create_database as db_creator

from zadanie39.corner import Corner, association_table
from zadanie39.well import Well
from zadanie39.field import Field


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()


    session = Session()

#вывести все углы наклона сквважины из таблицы corners
    print("*" * 10, "запрос 1", "*" * 10)
    for it in session.query(Corner):
        print(it.corner_title)
    print("*" * 50)

#вывести все вертикальные скважины (с углом наклона меньше 45 градусов)
    print("*" * 10, "запрос 2", "*" * 10)
    for it in session.query(Corner).filter(Corner.corner_title <= 45):
        print(it)
    print("*" * 50)
#Вывести какое количесвто скважин находится в БД
    print("*" * 10, "запрос 3", "*" * 10)
    print(session.query(Well).count())
    print("*" * 50)

#Вывести все скважины Газового месторождения
    print("*" * 10, "запрос 4", "*" * 10)
    for it in session.query(Well).join(Field).filter(Field.field_name == 'Газовое'):
        print(it)
    print("*" * 50)

# Вывести все скважины c номерами скважины меньше 2000
    print("*" * 10, "запрос 5", "*" * 10)
    for it in session.query(Well.num).filter(Well.num < 2000).distinct():
        print(it)
    print("*" * 50)

# Вывести данные о скважинах с глубинй меньше 3000 и с id меньше 15 по списку
    print("*" * 10, "запрос 6", "*" * 10)
    for it in session.query(Well).filter(Well.id < 15, Well.depth < 3000).distinct():
        print(it)
    print("*" * 50)

# Вывести данные по углу наклона скважин Нефтяного местрождения
    print("*" * 10, "запрос 7", "*" * 10)
    for it, gr in session.query(Corner.corner_title, Field.field_name).filter(
            and_(association_table.c.corner_id == Corner.id, association_table.c.field_id == Field.id,
                 Field.field_name == "Нефтяное")):
        print(it, gr)
    print("*" * 50)

# Вывести все нефтяные скважины в порядке возрастания номеров скважин
    print("*" * 10, "запрос 8", "*" * 10)
    for it in session.query(Well).filter(Well.field == 1).order_by(Well.num):
        print(it)
    print("*" * 50)

# Вывести газовые скважины с глубиной скважины менее 3000 метров, в порядке убывания номеров скважин
    print("*" * 10, "запрос 9", "*" * 10)
    for it in session.query(Well).filter(Well.field == 2, Well.depth < 3000).order_by(desc(Well.num)):
        print(it)
    print("*" * 50)

#Какие скважины с глубиной не более 2600 метров(малоглубинные)
    print("*" * 10, "запрос 10", "*" * 10)
    print(session.query(Well).filter(Well.depth.like("26%")).all())
    print("*" * 50)