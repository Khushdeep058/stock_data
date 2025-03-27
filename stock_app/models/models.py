from sqlalchemy import Column, TIMESTAMP, DECIMAL, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime

# Database Configuration
DATABASE_URL = "postgresql://postgres:khush952004@localhost:2004/stock_details"

engine = create_engine(DATABASE_URL)
Base = automap_base()
Base.prepare(engine, reflect=True)


StockData = Base.classes.stock_data


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class StockDataCreate(BaseModel):
    datetime: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    instrument: str

    class Config:
        from_attributes = True 
