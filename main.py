from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi.templating import Jinja2Templates


import models
from databases import engine, SessionLocal

models.Base.metadata.create_all(bind =engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

template = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")

class IncomingPost(BaseModel):
    Post: str
    Author: str
    Title: str

@app.get('/')
async def root():
    return {}

@app.get("/home/")
async def getAll(request: Request, db: Session = Depends(get_db)):

    AllPost = db.query(models.Post).all()

    AllContent = []

    for Now in AllPost:
        post = Now.Post
        Senten = post.split('.')
        truncated_post = '.'.join(Senten[:2])
        AllContent.append({
            'title': Now.Title, 
            "author": Now.Author,
            'post': truncated_post, 
            "likes": Now.Likes, 
            "dislikes": Now.Dislike,
            'date': Now.DatePosted,
            'id': Now.postId
        })
            
    context = {
        'request' : request,
        "content" : AllContent
    }
    return template.TemplateResponse("home.html", context)

@app.post('/PostContent/')
async def PostBlog(Incoming: IncomingPost,db: Session = Depends(get_db)):
    stmt = models.Post(
        Post = Incoming.Post,
        Author = Incoming.Author,
        Title = Incoming.Title
    )

    db.add(stmt)
    db.commit()

    return{"Message" : "Successful"}

@app.get('/getPost/{id}/{author}')
async def PostBlog(id: int, request:Request, db: Session = Depends(get_db)):
    stmt = db.query(models.Post).filter(models.Post.postId == id).first()

    context = {
        "request" : request,
        "thing":{
            "title": stmt.Title,
            "author": stmt.Author,
            "post" : stmt.Post,
            "likes": stmt.Likes,
            "dislikes": stmt.Dislike
        }
    }
    return template.TemplateResponse("post.html", context)

@app.get("/createContnet")
async def makingPost(request:Request):

    context = {
        "request": request
    }

    return template.TemplateResponse("makePost.html", context)


@app.put("/like/{id}/{author}")
async def ManageLikes():
    return{"Message": "WIP"}

@app.put("/dislike/{id}/{author}")
async def ManageDislikes():
    return{"Message": "WIP"}

@app.delete("/delete")
async def deleteAll(db: Session = Depends(get_db)):
    stmt = db.query(models.Post).delete()
    
    db.commit()


    return{"message": "Deletion completed"}

