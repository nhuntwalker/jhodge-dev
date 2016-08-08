from sqlalchemy import (
    Column,
    Date,
    Index,
    Integer,
    Unicode,
)

from .meta import Base


class Writing(Base):
    __tablename__ = 'writings'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    slug = Column(Unicode)
    published_on = Column(Date)
    publisher = Column(Unicode)
    publisher_link = Column(Unicode)
    excerpt = Column(Unicode)
    sample = Column(Unicode)
    cover_img = Column(Unicode)


Index('writing_idx', Writing.title, unique=True, mysql_length=255)
