from sqlalchemy import Column, ForeignKey, Integer, Table

from sqlalchemy.orm import relationship

from zadanie39.database import Base

association_table = Table('association', Base.metadata,
                          Column('corner_id', Integer, ForeignKey('corners.id')),
                          Column('field_id', Integer, ForeignKey('fields.id'))) #промежуточная таблица


class Corner(Base):
    __tablename__ = 'corners' #имя таблицы

    id = Column(Integer, primary_key=True)
    corner_title = Column(Integer, nullable=False)
    fields = relationship('Field', secondary=association_table, backref='field_corner')

    def __repr__(self):
        return f"Скважина с  (ID: {self.id}, Угол наклона: {self.corner_title})"

