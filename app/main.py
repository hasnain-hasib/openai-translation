from fastapi import FastAPI, BackgroundTasks,Request,Depends
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from app import schemas, crud, model
from app.database import engine, get_db

model.Base.metadata.create_all(bind= engine)

app = FastAPI()


templating = Jinja2Templates(directory="app/templates")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           
    allow_credentials=True,       
    allow_methods=["*"],           
    allow_headers=["*"],          
)
@app.get('/',response_class=HTMLResponse)

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templating.TemplateResponse("index.html", {"request": request})



@app.post('/translet',response_model=schemas.TaskResponse)
def translate (request: schemas.TranslationRequest, background_tasks :BackgroundTasks, db : Session  = Depends(get_db)):
     task = crud.create_Translation_Task(get_db, request.text, request.languages)

     background_tasks.add_task(perform_translation, task.id, request.text, request.languages, db)
     
     
     return