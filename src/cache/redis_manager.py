from redis import Redis
import json

class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = Redis(host=host, port=port, db=db)

    def set_checkpoint(self, key: str, value: dict):
        self.redis.set(key, json.dumps(value))

    def get_checkpoint(self, key: str) -> dict:
        value = self.redis.get(key)
        return json.loads(value) if value else None

    def delete_checkpoint(self, key: str):
        self.redis.delete(key)

    def clear_all_checkpoints(self):
        self.redis.flushdb()