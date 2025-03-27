from sqlalchemy.orm import Session
from service.service import get_all_stock_data, add_stock_data
from models.models import StockDataCreate

def fetch_all_stocks(db: Session):
    return get_all_stock_data(db)

def create_new_stock(stock_data: StockDataCreate, db: Session):
    return add_stock_data(db, stock_data)
