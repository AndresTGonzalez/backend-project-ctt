from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=80
    )
    description: str = Field(
        ...,
        min_length=5,
        max_length=200
    )
    price: float = Field(
        ...,
        gt=0 # Greater Than - Mayor que
    )
    stock: int = Field(
        ...,
        ge=0 # Greater than equal - Mayor o igual que
    )
    is_active: bool = Field(
        default= True
    )

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int