from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, order_detail):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        product_name=order_detail.product_name,
        quantity=order_detail.quantity
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


def update(db: Session, order_detail_id, order_detail):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_detail.first():
        raise HTTPException(status_code=404, detail="Order detail not found")

    update_data = order_detail.model_dump(exclude_unset=True)
    db_order_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_detail.first()


def delete(db: Session, order_detail_id):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_detail.first():
        raise HTTPException(status_code=404, detail="Order detail not found")

    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if not db_order_detail:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return db_order_detail
