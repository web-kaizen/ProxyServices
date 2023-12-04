from typing import Any, Optional

from django.conf import settings
from django.core.cache import cache


class Cache:

    def __init__(self) -> None:
        self.__cache = cache

    def set_value(self, key: str, value: Any, ttl: int = settings.CACHE_DEFAULT_TTL) -> None:
        """
        :param: timeout: seconds = 0 expires the value immediately.
                timeout: seconds = None infinite timeout

        Default value sets in the env file
        """
        self.__cache.set(key, value, ttl)

    def get_value(self, key: str) -> Any:
        """
        Returns None if the object does not exist
        """
        return self.__cache.get(key)

    def get_listed(self, keys: list) -> dict:
        """
        Return a dictionary with keys:values
        """
        return self.__cache.get_many(keys)

    def set_listed(self, keys: dict) -> None:
        return self.__cache.set_many(keys)

    def get_ttl(self, key: str) -> Optional[int]:
        """
        - 0 (False) if key does not exist (or already expired).
        - None for keys that exists but does not have any expiration.
        - ttl value (seconds) for any volatile key (any key that has expiration).
        """
        return self.__cache.ttl(key)

    def remove(self, key: str) -> bool:
        """
        Returns True if key:value is deleted
        """
        return self.__cache.delete(key)

    def remove_all(self) -> None:
        """
        Deletes all key:values from cache
        """
        return self.__cache.clear()
