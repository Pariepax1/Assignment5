from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PaymentBase(BaseModel):
    card_number: str
    transaction_status: str
    payment_type: str
    amount: float


class PaymentCreate(PaymentBase):
    order_id: int  # Foreign key linking to an order


class PaymentUpdate(BaseModel):
    card_number: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None
    amount: Optional[float] = None


class Payment(PaymentBase):
    id: int
    order_id: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True
