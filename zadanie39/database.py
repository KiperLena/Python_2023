from sqlalchemy import create_engine #импорт для создания настроек
from sqlalchemy.ext.declarative import declarative_base #для определения таблиц и моделей
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'well.db'

engine = create_engine(f"sqlite:///{DATABASE_NAME}") #создаст базу данных с указанным названием
Session = sessionmaker(bind=engine) #отвечает за все запросы
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine) #добавить классы в виде таблиц в БД
