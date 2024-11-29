from fastapi import APIRouter
from . import (
    orders,
    order_details,
    customers,
    payments,
    promotions,
    reviews,
    recipes
)

# Create the APIRouter instance
router = APIRouter()

# Load routes for the app
def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(payments.router)
    app.include_router(promotions.router)
    app.include_router(reviews.router)
    app.include_router(recipes.router)

# Example route for index
@router.get("/")
def index():
    return {"message": "API Index"}
