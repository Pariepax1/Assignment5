from sqlalchemy import Column, Integer, String, Text, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    review_text = Column(Text, nullable=False)
    score = Column(Integer, nullable=False)  # e.g., 1-5 rating
    created_at = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    customer = relationship("Customer", back_populates="reviews")
    order = relationship("Order", back_populates="reviews")
