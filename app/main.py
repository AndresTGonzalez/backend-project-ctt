from fastapi import FastAPI
from app.routes.health_routes import health_router
from app.routes.product_routes import product_router

app = FastAPI(
    title="CTT Course",
    description="CTT Course of FISEI",
    version="1.0.0"
)


app.include_router(router=health_router)
app.include_router(router=product_router)