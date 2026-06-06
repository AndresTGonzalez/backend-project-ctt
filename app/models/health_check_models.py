from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str
    service_name: str