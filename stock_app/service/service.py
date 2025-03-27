from sqlalchemy.orm import Session
from models.models import StockData,StockDataCreate


def get_all_stock_data(db: Session):
    return db.query(StockData).all()

def add_stock_data(db: Session, stock_data: StockDataCreate):
    new_stock = StockData(**stock_data.dict())
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

