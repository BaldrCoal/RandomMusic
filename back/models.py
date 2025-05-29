from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship

from database import Base


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
    data = Column(LargeBinary)
