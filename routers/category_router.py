from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from models.category import Category
from database import get_db
from schema.category_schema import CategorySchema

router = APIRouter()

@router.post("/categories", response_model=CategorySchema)
def add_category(category: CategorySchema, db: Session = Depends(get_db)):
    """
    API thêm mới danh mục.
    """
    new_category = Category(
        name=category.name,
        parent_category_id=category.parent_category_id,
        level=category.level,
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return CategorySchema.from_orm(new_category)

@router.get("/categories/{category_id}", response_model=CategorySchema)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    """
    API lấy danh mục theo ID.
    """
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return CategorySchema.from_orm(category)

@router.get("/categories", response_model=List[CategorySchema])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).options(joinedload(Category.subcategories)).all()
    return [CategorySchema.from_orm(category) for category in categories]
