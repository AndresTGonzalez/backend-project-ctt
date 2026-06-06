from fastapi import APIRouter

from app.models.health_check_models import HealthCheck
from app.services.health_services import HealthServices

health_router = APIRouter(prefix="/health", tags=["Health"])
health = HealthServices()



@health_router.get("/")
def get_health_api () -> HealthCheck:
    
    return health.get_health()