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
    release_date = Column(Unicode)
    production = Column(Unicode)
    slug = Column(Unicode)
    excerpt = Column(Unicode)
    slider_text = Column(Unicode)
    home_text = Column(Unicode)
    full_text = Column(Unicode)
    trailer = Column(Unicode)
    screenshot = Column(Unicode)


Index('film_idx', Film.title, unique=True, mysql_length=255)
