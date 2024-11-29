from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    card_number = Column(String(16), nullable=False)
    transaction_status = Column(String(50), nullable=False)
    payment_type = Column(String(50), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    order = relationship("Order", back_populates="payments")
