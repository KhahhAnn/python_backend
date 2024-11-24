from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from exception.product_exception import ProductException
from models.user import Users
from response.api_response import ApiResponse  # Giả sử có file này để định dạng response
from service.ratting_service import RatingService
from database import get_db
from request.rating_request import RatingRequest  # Giả sử có file này để nhận dữ liệu từ client
from schema.rating_schema import RatingSchema

router = APIRouter()

# Route để tạo đánh giá cho sản phẩm
@router.post("/rating", response_model=RatingSchema)
def create_rating(
    req: RatingRequest,
    user: Users,
    db: Session = Depends(get_db),
    service: RatingService = Depends(),
):
    try:
        return service.create_rating(req, user)
    except ProductException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route để lấy tất cả đánh giá của sản phẩm
@router.get("/rating/{product_id}", response_model=List[RatingSchema])
def get_products_rating(product_id: int, db: Session = Depends(get_db), service: RatingService = Depends()):
    try:
        return service.get_products_rating(product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route để cập nhật đánh giá
@router.put("/rating/{rating_id}", response_model=RatingSchema)
def update_rating(
    rating_id: int, req: RatingRequest, user: Users, db: Session = Depends(get_db), service: RatingService = Depends()
):
    try:
        return service.update_rating(rating_id, req, user)
    except RatingException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route để xóa đánh giá
@router.delete("/rating/{rating_id}", response_model=RatingResponse)
def delete_rating(rating_id: int, user: Users, db: Session = Depends(get_db), service: RatingService = Depends()):
    try:
        service.delete_rating(rating_id, user)
        return {"detail": "Rating deleted successfully"}
    except RatingException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
