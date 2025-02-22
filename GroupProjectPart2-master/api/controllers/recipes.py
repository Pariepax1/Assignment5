from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import recipes as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_recipe = model.Recipe(
        sandwich_id=request.sandwich_id,
        resource_id=request.resource_id,
        amount=request.amount
    )
    try:
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_recipe


def read_all(db: Session):
    try:
        result = db.query(model.Recipe).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, recipe_id):
    try:
        recipe = db.query(model.Recipe).filter(model.Recipe.id == recipe_id).first()
        if not recipe:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return recipe


def update(db: Session, recipe_id, request):
    try:
        recipe = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
        if not recipe.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!")
        update_data = request.dict(exclude_unset=True)
        recipe.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return recipe.first()


def delete(db: Session, recipe_id):
    try:
        recipe = db.query(model.Recipe).filter(model.Recipe.id == recipe_id)
        if not recipe.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!")
        recipe.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
