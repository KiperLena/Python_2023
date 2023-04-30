from sqlalchemy import Column, ForeignKey, Integer, String, Table

from sqlalchemy.orm import relationship

from DZ39.database import Base

association_table = Table('association', Base.metadata,
                          Column('corner_id', Integer, ForeignKey('corner.id')),
                          Column('group_id', Integer, ForeignKey('field.id')))


class Corner(Base):
    __tablename__ = 'corner'

    id = Column(Integer, primary_key=True)
    corner_title = Column(String(250), nullable=False)
    groups = relationship('Field', secondary=association_table, backref='group_corner')

    def __repr__(self):
        return f"Скважина с  (ID: {self.id}, Угол наклона: {self.corner_title})"

