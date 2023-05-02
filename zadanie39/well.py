from sqlalchemy import Column, ForeignKey, Integer

from zadanie39.database import Base


class Well(Base):
    __tablename__ = 'well'

    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False)  # nullable=False - поле обязательное для заполнения
    depth = Column(Integer, nullable=False)
    field = Column(Integer, ForeignKey('fields.id')) #связь с таблицей через id

    def __init__(self, num, depth, id_field):
        self.num = num
        self.depth = depth
        self.field = id_field

    def __repr__(self):
        return f"Скважина (№: {self.num} , " \
               f"Глубина: {self.depth}, ID месторождения: {self.field})"








