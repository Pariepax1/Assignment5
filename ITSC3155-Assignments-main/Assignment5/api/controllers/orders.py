from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, status
from ..models import models


def create(db: Session, order):
    db_order = models.Order(
        customer_name=order.customer_name,
        description=order.description
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def read_all(db: Session):
    return db.query(models.Order).all()


def read_one(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


def update(db: Session, order_id: int, order):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    if not db_order.first():
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = order.model_dump(exclude_unset=True)
    db_order.update(update_data, synchronize_session=False)
    db.commit()
    return db_order.first()


def delete(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    if not db_order.first():
        raise HTTPException(status_code=404, detail="Order not found")

    db_order.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
