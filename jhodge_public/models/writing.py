from sqlalchemy import (
    Column,
    Date,
    Index,
    Integer,
    Unicode,
    Boolean
)

from .meta import Base


class Writing(Base):
    __tablename__ = 'writings'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    published_on = Column(Unicode)
    publisher = Column(Unicode)
    slug = Column(Unicode)
    full_text = Column(Unicode)
    center = Column(Boolean)
    external_link = Column(Unicode)
    cover_img = Column(Unicode)


Index('writing_idx', Writing.title, unique=True, mysql_length=255)
