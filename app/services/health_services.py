from app.models.health_check_models import HealthCheck


class HealthServices():
    def get_health(self) -> HealthCheck:
        return HealthCheck(
            status="ok",
            service_name="CTT Course"
        )