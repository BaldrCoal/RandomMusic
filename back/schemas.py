from pydantic import BaseModel


class SongBase(BaseModel):
    title: str
    artist: str


class SongUpload(SongBase):
    data: bytes


class Song(SongBase):
    id: int

    class Config:
        orm_mode = True
