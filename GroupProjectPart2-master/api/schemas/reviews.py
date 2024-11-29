from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ReviewBase(BaseModel):
    review_text: str
    score: int  # Rating score, e.g., 1-5


class ReviewCreate(ReviewBase):
    customer_id: int  # Foreign key linking to a customer
    order_id: Optional[int] = None  # Optional link to an order


class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[int] = None
    customer_id: Optional[int] = None
    order_id: Optional[int] = None


class Review(ReviewBase):
    id: int
    customer_id: int
    order_id: Optional[int]
    created_at: datetime

    class ConfigDict:
        from_attributes = True
