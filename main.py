from fastapi import FastAPI
from routers import (category_router, product_router, address_router, account_router, admin_product_router,
                     order_router, order_item_router, cart_item_router, cart_router, review_router, rating_router, customer_user_service)

# from routers import product_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application with MySQL and Email!"}


app.include_router(category_router.router, prefix="/api", tags=["Categories"])
app.include_router(product_router.router, prefix="/api", tags=["Products"])
app.include_router(address_router.router, prefix="/api", tags=["Address"])
app.include_router(account_router.router, prefix="/api", tags=["Account"])
app.include_router(admin_product_router.router, prefix="/api", tags=["AdminProduct"])
app.include_router(order_router.router, prefix="/api", tags=["Order"])
app.include_router(order_item_router.router, prefix="/api", tags=["OrderItem"])
app.include_router(cart_item_router.router, prefix="/api", tags=["CartItem"])
app.include_router(cart_router.router, prefix="/api", tags=["Cart"])
app.include_router(rating_router.router, prefix="/api", tags=["Ratting"])
app.include_router(customer_user_service.router, prefix="/api", tags=["CustomerUser"])
app.include_router(review_router.router, prefix="/api", tags=["Review"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
