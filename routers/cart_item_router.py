from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.cart import Cart
from models.cartItem import CartItem
from service.cart_item_service import CartItemService
from database import get_db

router = APIRouter()

# Dependency to inject CartItemService
def get_cart_item_service(db: Session = Depends(get_db)) -> CartItemService:
    return CartItemService(db=db)

# Add product to cart
@router.post("/cart-items")
async def create_cart_item(cart_item: CartItem, db: Session = Depends(get_db), cart_item_service: CartItemService = Depends(get_cart_item_service)):
    try:
        new_cart_item = cart_item_service.create_cart_item(cart_item)
        return {"message": "Cart item added successfully", "cart_item": new_cart_item}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Update cart item (quantity)
@router.put("/cart-items/{cart_item_id}")
async def update_cart_item(cart_item_id: int, cart_item: CartItem, db: Session = Depends(get_db), cart_item_service: CartItemService = Depends(get_cart_item_service)):
    try:
        updated_cart_item = cart_item_service.update_cart_item(user_id=cart_item.cart_id, cart_item_id=cart_item_id, cart_item=cart_item)
        return {"message": "Cart item updated successfully", "cart_item": updated_cart_item}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Remove product from cart
@router.delete("/cart-items/{cart_item_id}")
async def remove_cart_item(cart_item_id: int, db: Session = Depends(get_db), cart_item_service: CartItemService = Depends(get_cart_item_service)):
    try:
        cart_item_service.remove_cart_item(cart_item_id)
        return {"message": "Cart item removed successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get all items in the cart (for user)
@router.get("/cart-items/{cart_id}")
async def get_cart_items(cart_id: int, db: Session = Depends(get_db), cart_item_service: CartItemService = Depends(get_cart_item_service)):
    try:
        cart_items = db.query(CartItem).filter(CartItem.cart_id == cart_id).all()
        if not cart_items:
            raise HTTPException(status_code=404, detail="No items found in the cart")
        return {"cart_items": cart_items}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
