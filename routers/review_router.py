from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from exception.product_exception import ProductException
from models.user import Users

from schema.review_schema import ReviewSchema
from service.review_service import ReviewService
from database import get_db
from request.review_request import ReviewRequest  # Giả sử có file này để nhận dữ liệu từ client

router = APIRouter()

# Route để tạo đánh giá cho sản phẩm
@router.post("/review", response_model=ReviewSchema)
def create_review(
    req: ReviewRequest,
    user: Users,
    db: Session = Depends(get_db),
    service: ReviewService = Depends(),
):
    try:
        return service.create_review(req, user)
    except ProductException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route để lấy tất cả đánh giá của sản phẩm
@router.get("/review/{product_id}", response_model=List[ReviewSchema])
def get_products_review(product_id: int, db: Session = Depends(get_db), service: ReviewService = Depends()):
    try:
        return service.get_products_review(product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route để xóa đánh giá
@router.delete("/review/{review_id}", response_model=ReviewSchema)
def delete_review(review_id: int, db: Session = Depends(get_db), service: ReviewService = Depends()):
    try:
        service.delete_review(review_id)
        return {"detail": "Review deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
