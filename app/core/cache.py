import redis

from app.core.settings import get_settings

settings = get_settings()

redis_client = redis.Redis.from_url(
    url=settings.REDIS_URL, 
    decode_responses = True
)