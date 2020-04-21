from app.db import Base
from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer, String, Table, Date, Float, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
import uuid
import datetime


def _generate_id():
    return uuid.uuid4()


def _get_date():
    return datetime.datetime.utcnow()


metadata = Base.metadata


# -----------------------------------------------------------------------------
# CLASS IDENTITY TYPE
# -----------------------------------------------------------------------------
class IdentityType(Base):

    __tablename__ = 'identity_type'

    # Columns
    type_name = Column(String(80), primary_key=True, index=True, nullable=False)

    # Relationships
    identities = relationship("Identity", back_populates="identity_type")


# -----------------------------------------------------------------------------
# CLASS IDENTITY
# -----------------------------------------------------------------------------
class Identity(Base):

    __tablename__ = 'identity'

    # Columns
    id = Column(UUID, primary_key=True, index=True, nullable=False)
    username = Column(String(120), unique=True, index=True, nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password_hash = Column(String(1024), nullable=False)
    salt = Column(String(30), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    last_login = Column(DateTime, nullable=True)
    created = Column(DateTime, nullable=True)
    identity_type_id = Column(String(80), ForeignKey("identity_type.type_name"))
    attrs = Column(JSONB(astext_type=Text()), nullable=True)

    # Relationships
    identity_type = relationship("IdentityType", back_populates="identities")





