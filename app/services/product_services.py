import json
from math import ceil

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product_models import (
    PaginatedProductResponse,
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)
from app.core.cache import redis_client


def _invalidate_products_list_cache() -> None:
    for key in redis_client.scan_iter("products:active:list*"):
        redis_client.delete(key)


class ProductServices():
    def __init__(self):
        pass

    def get_all_products(
        self, db: Session, page: int, page_size: int
    ) -> PaginatedProductResponse:
        cache_key = f"products:active:list:page:{page}:size:{page_size}"
        cached_products = redis_client.get(cache_key)

        if cached_products:
            return PaginatedProductResponse.model_validate(json.loads(cached_products))

        offset = (page - 1) * page_size

        total = db.scalar(
            select(func.count()).select_from(Product).where(Product.is_active)
        ) or 0

        products = db.scalars(
            select(Product)
            .where(Product.is_active)
            .offset(offset)
            .limit(page_size)
        ).all()

        total_pages = ceil(total / page_size) if total > 0 else 0

        response = PaginatedProductResponse(
            items=[ProductResponse.model_validate(product) for product in products],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

        redis_client.setex(
            name=cache_key,
            time=3600,
            value=json.dumps(response.model_dump(mode="json")),
        )

        return response

    def get_product(self, product_id: int, db: Session) -> ProductResponse | None:
        product = db.get(Product, product_id)
        return product

    def create_product(self, product_data: ProductCreate, db: Session) -> ProductResponse:
        product = Product(
            **product_data.model_dump()
        )
        db.add(product)
        db.commit()
        db.refresh(product)

        _invalidate_products_list_cache()

        return product

    def update_product(self, product_id: int, product_data: ProductUpdate, db: Session) -> ProductResponse | None:
        product = db.get(Product, product_id)
        if not product:
            return None

        update_data = product_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(product, field, value)

        db.commit()
        db.refresh(product)

        _invalidate_products_list_cache()

        return product

    def delete_product(self, product_id: int, db: Session) -> bool:
        product = db.get(Product, product_id)
        if not product:
            return False

        db.delete(product)
        db.commit()

        _invalidate_products_list_cache()

        return True

