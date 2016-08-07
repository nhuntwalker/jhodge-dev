from sqlalchemy import (
    Column,
    Date,
    Index,
    Integer,
    Unicode,
)

from .meta import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    email = Column(Unicode)
    subject = Column(Unicode)
    message = Column(Unicode)


Index('contact_idx', Contact.name, unique=True, mysql_length=255)
