from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import engine,SessionLocal
import models
import schemas

from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"]

)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/expense")
def expenses(
    expense:schemas.ExpCreate,
    db:Session=Depends(get_db)
):
    new_expense=(models.Exptracker(
        title=expense.title,
        amount=expense.amount
    ))
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.get("/expense")
def get_Expenses(
    db:Session=Depends(get_db)
):
    expense=db.query(models.Exptracker).all()
    return expense

@app.put("/expense/{id}")
def change_expense(
    id:int,
    expense:schemas.ExpCreate,
    db:Session=Depends(get_db)
):
    new_expense=(db.query(models.Exptracker)
    .filter(models.Exptracker.id==id)
    .first()
    )

    if not new_expense:
        return {"message":"id not found"}
    
    new_expense.title=expense.title
    new_expense.amount=expense.amount

    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.delete("/expense/{id}")
def change_expense(
    id:int,
    db:Session=Depends(get_db)
):
    new_expense=(db.query(models.Exptracker)
    .filter(models.Exptracker.id==id)
    .first()
    )

    if not new_expense:
        return {"message":"id not found"}
    
    db.delete(new_expense)

    db.commit()
