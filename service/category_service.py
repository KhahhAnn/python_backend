from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.category import Category
from repository.category_repository import CategoryRepository
from response.api_response import ApiResponse


class CategoryService:
    def __init__(self, category_repository: CategoryRepository = Depends(), db: Session = Depends(get_db)):
        self.category_repository = category_repository
        self.db = db

    def update_category(self, category: Category) -> Category:
        existing_category = self.category_repository.get_reference_by_id(category.id)
        if not existing_category:
            raise HTTPException(status_code=404, detail="Category not found")

        existing_category.name = category.name
        self.db.commit()
        self.db.refresh(existing_category)
        return existing_category

    def add_category(self, category: Category) -> ApiResponse:
        response = ApiResponse()

        if self.category_repository.find_by_name(category.name):
            response.status = False
            response.message = "Addition failed: Category name already exists"
            return response

        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        response.status = True
        response.message = "Category added successfully"
        return response

    def delete_category(self, category_id: int) -> ApiResponse:
        response = ApiResponse()

        category = self.category_repository.get_reference_by_id(category_id)
        if not category:
            response.status = False
            response.message = "Deletion failed: Category not found"
            return response

        category.parent_category = None
        self.db.delete(category)
        self.db.commit()

        response.status = True
        response.message = "Category deleted successfully"
        return response
