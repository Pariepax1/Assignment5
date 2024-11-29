from sqlalchemy import Column, Integer, String, DATETIME
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_percentage = Column(Integer, nullable=False)
    expiration_date = Column(DATETIME, nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
