from typing import Union

from fastapi import FastAPI, Request, Depends, HTTPException
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import crud, models, schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
templates = Jinja2Templates(directory="../front/templates")
app.mount("/static", StaticFiles(directory="../front"), name="static")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/song", response_class=HTMLResponse)
async def get_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home Page", "name": "FastAPI User"})


@app.post("/songs/", response_model=schemas.Song)
def upload_song(song: schemas.SongUpload, db: Session = Depends(get_db)):
    db_song = crud.get_song_by_title(db, title=song.title)
    if db_song:
        raise HTTPException(status_code=400, detail="Song already exists")
    return crud.upload_song(db=db, song=song)
