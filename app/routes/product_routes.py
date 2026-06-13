from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product_models import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_services import ProductServices

product_router = APIRouter(prefix="/products", tags=["Products"])
product_service = ProductServices()

@product_router.get("/")
def get_all_products_api(db: Session = Depends(get_db)) -> list[ProductResponse]:
    return product_service.get_all_products(db=db)

@product_router.get("/{product_id}")
def get_product_api(product_id: int, db: Session = Depends(get_db)) -> ProductResponse | None:
    return product_service.get_product(db=db, product_id=product_id)

@product_router.post("/")
def create_product_api (product_data: ProductCreate, db: Session = Depends(get_db)) -> ProductResponse:
    return product_service.create_product(product_data=product_data, db=db)

@product_router.put("/{product_id}")
def update_product_api(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)) -> ProductResponse | None:
    return product_service.update_product(db=db, product_id=product_id, product_data=product_data)

@product_router.delete("/{product_id}")
def delete_product_api(product_id: int, db: Session = Depends(get_db)) -> bool:
    return product_service.delete_product(product_id=product_id, db=db)