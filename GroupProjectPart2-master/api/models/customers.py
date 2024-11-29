from sqlalchemy import Column, Integer, String, Text, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    created_at = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    updated_at = Column(DATETIME, nullable=False, server_default=str(datetime.now()), onupdate=str(datetime.now()))

    # Relationship with reviews
    reviews = relationship("Review", back_populates="customer")
