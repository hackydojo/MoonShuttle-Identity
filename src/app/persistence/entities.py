from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime


def _generate_id():
    return uuid.uuid4()


def _get_date():
    return datetime.datetime.utcnow()


Base = declarative_base()
metadata = Base.metadata
