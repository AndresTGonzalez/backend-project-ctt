from app.models.product_models import ProductCreate, ProductResponse, ProductUpdate


class ProductServices():

    # public List<ProductResponse> products = new ArrayList<ProductResponse>();
    # public int nextId = 1


    def __init__(self):
        self.products: list[ProductResponse] = []
        self.next_id: int = 1

    def get_all_products(self) -> list[ProductResponse]: 
        return self.products

    def get_product(self, product_id: int) -> ProductResponse | None:
        # Para cada producto en mi listado de productos haz esto:
        # Verifica si el id del producto que estas recorriendo es igual al id del parametro recibido
        # Si coinciden devuelvelo, caso contrario avanza y termina de recorrer
        # Si no coincide ninguno retorna un Null o un None
        for product in self.products:
            if product.id == product_id:
                return product
        
        return None

    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        new_product = ProductResponse(
            id=self.next_id,
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            stock=product_data.stock,
            is_active=product_data.is_active
        )

        self.products.append(new_product)
        self.next_id += 1

        return new_product

    def update_product(self, product_id: int, product_data: ProductUpdate) -> ProductResponse | None:
        for index, product in enumerate(self.products):
            if product.id == product_id:
                update_product = ProductResponse(
                    id=product_id,
                    name=product_data.name,
                    description=product_data.description,
                    price=product_data.price,
                    stock=product_data.stock,
                    is_active=product_data.is_active
                )
                self.products[index] = update_product
                return update_product
            
        return None

    def delete_product(self, product_id: int) -> bool:
        for index, product in enumerate(self.products):
            if product.id == product_id:
                self.products.pop(index)
                return True
            
        return False


# CRUD
# C = Create
# R = Read
# U = Update
# D = Delete