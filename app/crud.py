from sqlalchemy.orm import Session

from app import model

def create_Translation_Task(db:Session , text : str, languages: list):
    task = model.TranslationTask(text = text, language = languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task 

def get_translation_task(db : Session, task_id : int):
    return db.query(model.TranslationTask).filter(model.TranslationTask.id == task_id).first()
    
    
def update_translation_task (db: Session, task_id: int, translation :dict):
    task = db.query(model.TranslationTask).filter(model.TranslationTask.id == task_id ).first()
    task.translation  = translation
    task.status = "completed"
    db.commit()
    db.refresh(task)
    return task




