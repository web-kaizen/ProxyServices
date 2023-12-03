from typing import Any, Optional

from django.conf import settings
from django.core.cache import cache


class RedisCacheManager:

    def __init__(self) -> None:
        self.cache = cache

    def set_key(self, key: str, value: Any, timeout: int = settings.CACHE_DEFAULT_TTL) -> None:
        """
        :param: timeout: seconds = 0 expires the value immediately.
                timeout: seconds = None infinite timeout

        Default value sets in the env file
        """
        self.cache.set(key, value, timeout=timeout)

    def get_value_by_key(self, key: str) -> Any:
        return self.cache.get(key)

    def get_keys_time_to_live(self, key: str) -> Optional[int]:
        """
        - 0 (False) if key does not exist (or already expired).
        - None for keys that exists but does not have any expiration.
        - ttl value (seconds) for any volatile key (any key that has expiration).
        """
        return self.cache.ttl(key)

    def remove_key(self, keys_pattern: str) -> int:
        """
        Returns the number of deleted keys
        """
        return self.cache.delete_pattern(keys_pattern)
