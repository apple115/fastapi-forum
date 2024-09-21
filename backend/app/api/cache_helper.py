from fastapi import HTTPException
import redis
from redis.commands.json.path import Path
from loguru import logger
from sqlmodel import SQLModel, Session
from typing import Callable, TypeVar, Any


T = TypeVar("T", bound=SQLModel)


def get_or_cache_item(
    redis_client: redis.Redis,
    session: Session,
    cache_key: str,
    db_lookup_func: Callable[..., None | T],
    db_lookup_func_args: dict[str, Any],
)->T :
    try:
        cache_item: T|None = redis_client.json().get(cache_key, Path.root_path())
        if cache_item :
            logger.info(f"Cache hit for {cache_key}")
            return cache_item
    except Exception as redis_error:
        logger.error(f"Redis error: {redis_error}")

    item = db_lookup_func(**db_lookup_func_args)
    if item is None:
        raise HTTPException(
            status_code=404, detail=f"Item with key {cache_key} not found"
        )
    try:
        # 将数据库中的结果缓存
        redis_client.json().set(cache_key, Path.root_path(), item.model_json_schema())
        logger.info(f"Cached item {cache_key} in Redis")
    except Exception as redis_error:
        logger.error(f"Failed to cache item {cache_key} in Redis: {redis_error}")
    return item
