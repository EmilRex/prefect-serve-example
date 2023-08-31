import platform

from prefect import flow, get_run_logger


@flow
def hello(name: str):
    logger = get_run_logger()
    logger.info(f"Hello from {platform.node()}, {name}!")
