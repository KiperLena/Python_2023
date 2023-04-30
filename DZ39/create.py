from faker import Faker

from DZ39.database import create_db, Session
from DZ39.corner import Corner
from DZ39.well import Well
from DZ39.field import Field


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    corner_names = [30, 45, 70, 80, 90]

    field1 = Field(field_name="Нефтяное")
    field2 = Field(field_name="Газовое")
    session.add(field1)
    session.add(field2)

    for key, it in enumerate(corner_names):
        corner = Corner(corner_title=it)
        corner.field.append(field1)
        if key % 2 == 0:
            corner.field.append(field2)
        session.add(corner)

    faker = Faker('ru_RU')
    field_list = [field1, field2]
    session.commit()

    for _ in range(50):
        num = faker.random.randint(1000, 2000)
        depth = faker.random.randint(2500, 3500)
        group = faker.random.choice(field_list)
        well = Well(num, depth, group.id)
        session.add(well)

    session.commit()
    session.close()
