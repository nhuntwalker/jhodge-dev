from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    Date
)

from .meta import Base


class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    release_date = Column(Date)
    production = Column(Unicode)
    production_link = Column(Unicode)
    director = Column(Unicode)
    cast = Column(Unicode)
    excerpt = Column(Unicode)
    trailer = Column(Unicode)
    snapshot = Column(Unicode)


Index('film_idx', Film.title, unique=True, mysql_length=255)
