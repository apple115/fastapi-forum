import logging
from sqlmodel import Session
from app.core.db import engine, init_db,create_db_and_tables


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    create_db_and_tables()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
