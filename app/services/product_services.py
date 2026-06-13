from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product_models import ProductCreate, ProductResponse, ProductUpdate


class ProductServices():
    def __init__(self):
        pass


    def get_all_products(self, db: Session) -> list[ProductResponse]: 
        products = db.scalars(
            select(Product).where(Product.is_active == True)
        ).all()
        return products

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

        return product

    def delete_product(self, product_id: int, db: Session) -> bool:
        product = db.get(Product, product_id)
        if not product:
            return False
        
        db.delete(product)
        db.commit()

        return True


