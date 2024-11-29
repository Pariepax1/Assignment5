from datetime import datetime
from pydantic import BaseModel
from typing import Optional  # Add this import

class PromotionBase(BaseModel):
    code: str
    discount_percentage: int
    expiration_date: datetime


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount_percentage: Optional[int] = None
    expiration_date: Optional[datetime] = None


class Promotion(PromotionBase):
    id: int
    created_at: datetime

    class ConfigDict:
        from_attributes = True
