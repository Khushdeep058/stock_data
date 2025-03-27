from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from controller.controller import fetch_all_stocks, create_new_stock
from models.models import StockDataCreate, SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/data")
def get_stock_data(db: Session = Depends(get_db)):
    return fetch_all_stocks(db)


@router.post("/new_stock")
def new_stock_data(stock_data: StockDataCreate, db: Session = Depends(get_db)):
    return create_new_stock(stock_data, db)

@router.post("/data")
async def post_stock_data(stock_data: StockDataCreate):
    return {"message": "Valid data"}