from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import (
    index_router,
    customers_router,
    orders_router,
    order_details_router,
    payments_router,
    promotions_router,
    reviews_router,
    recipes_router,
    resources_router,
    sandwiches_router,
)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(index_router)
app.include_router(customers_router)
app.include_router(orders_router)
app.include_router(order_details_router)
app.include_router(payments_router)
app.include_router(promotions_router)
app.include_router(reviews_router)
app.include_router(recipes_router)
app.include_router(resources_router)
app.include_router(sandwiches_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
