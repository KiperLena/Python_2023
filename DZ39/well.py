from sqlalchemy import Column, ForeignKey, Integer, String

from DZ39.database import Base

class Well(Base):
    __tablename__ = 'well'

    id = Column(Integer, primary_key=True)
    num = Column(Integer, nullable=False)  # nullable=False - поле обязательное для заполнения
    depth = Column(Integer)
    group = Column(Integer, ForeignKey('field.id'))

    def __init__(self, num, depth, id_group):
        self.num = num
        self.depth = depth
        self.group = id_group


   def __repr__(self):
        return f"Скважина (№: {self.num} , " \
               f"Глубина: {self.depth}, ID месторождения: {self.group})"






