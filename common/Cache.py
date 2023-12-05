from typing import Any, Optional

from django.conf import settings
from django.core.cache import cache


class Cache:

    @staticmethod
    def set_value(key: str, value: Any, ttl: int = settings.CACHE_DEFAULT_TTL) -> None:
        """
        :param: timeout: seconds = 0 expires the value immediately.
                timeout: seconds = None infinite timeout

        Default value sets in the env file
        """
        cache.set(key, value, ttl)

    @staticmethod
    def get_value(key: str) -> Any:
        """
        Returns None if the object does not exist
        """
        return cache.get(key)

    @staticmethod
    def get_listed(keys: list) -> dict:
        """
        Return a dictionary with keys:values
        """
        return cache.get_many(keys)

    @staticmethod
    def set_listed(keys: dict) -> None:
        return cache.set_many(keys)

    @staticmethod
    def get_ttl(key: str) -> Optional[int]:
        """
        Returns:
            - 0 (False) if key does not exist (or already expired).
            - None for keys that exists but does not have any expiration.
            - ttl value (seconds) for any volatile key (any key that has expiration).
        """
        return cache.ttl(key)

    @staticmethod
    def remove(key: str) -> bool:
        """
        Returns True if key:value is deleted
        """
        return cache.delete(key)

    @staticmethod
    def remove_all() -> None:
        """
        Deletes all key:values from cache
        """
        return cache.clear()
