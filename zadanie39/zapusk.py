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
