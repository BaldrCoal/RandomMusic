from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas


def get_song(db: Session, song_id: int):
    return db.query(models.Song).filter(models.Song.id == song_id).first()


def get_song_by_title(db: Session, title: str):
    return db.query(models.Song).filter(models.Song.title == title).first()


def get_song_by_artist(db: Session, artist: str):
    return db.query(models.Song).filter(models.Song.artist == artist).first()


def get_songs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Song).offset(skip).limit(limit).all()


def upload_song(db: Session, song: schemas.SongUpload):
    db_song = models.Song(title=song.title, artist=song.artist, data=song.data)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song
