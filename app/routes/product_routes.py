from fastapi import APIRouter

from app.models.product_models import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_services import ProductServices

product_router = APIRouter(prefix="/products", tags=["Products"])
product_service = ProductServices()

@product_router.get("/")
def get_all_products_api() -> list[ProductResponse]:
    return product_service.get_all_products()

@product_router.get("/{product_id}")
def get_product_api(product_id: int) -> ProductResponse | None:
    return product_service.get_product(product_id=product_id)

@product_router.post("/")
def create_product_api (product_data: ProductCreate) -> ProductResponse:
    return product_service.create_product(product_data=product_data)

@product_router.put("/{product_id}")
def update_product_api(product_id: int, product_data: ProductUpdate) -> ProductResponse | None:
    return product_service.update_product(product_id=product_id, product_data=product_data)

@product_router.delete("/{product_id}")
def delete_product_api(product_id: int) -> bool:
    return product_service.delete_product(product_id=product_id)