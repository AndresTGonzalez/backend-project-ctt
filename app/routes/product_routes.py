from fastapi import APIRouter

from app.schemas.product_models import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_services import ProductServices

product_router = APIRouter(prefix="/products", tags=["Products"])
product_service = ProductServices()

@product_router.get("/")
def get_all_products_api() -> list[ProductResponse]:
    pass

@product_router.get("/{product_id}")
def get_product_api(product_id: int) -> ProductResponse | None:
    pass

@product_router.post("/")
def create_product_api (product_data: ProductCreate) -> ProductResponse:
    pass

@product_router.put("/{product_id}")
def update_product_api(product_id: int, product_data: ProductUpdate) -> ProductResponse | None:
    pass

@product_router.delete("/{product_id}")
def delete_product_api(product_id: int) -> bool:
    pass