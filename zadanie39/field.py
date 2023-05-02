from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from zadanie39.database import Base


class Field(Base):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True)
    field_name = Column(String(250), nullable=False)
    well = relationship('Well') #связь межтабличная и не влияет на БД(служебная)

    def __repr__(self):
        return f"Месторождение (ID: {self.id}, Название: {self.field_name})"

