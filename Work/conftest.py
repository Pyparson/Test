import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(scope="module")
def module():
    logging.info("This is setup_module!!!")


@pytest.fixture(scope="class")
def classA_end():
    logging.info("This is ClassA teardown_class")
    yield
    logging.info("Clean the venv...")


# @pytest.fixture(autouse=True)   # autouse=True可以实现全局
@pytest.fixture()
def classB_start():
    logging.info("This is ClassB setup_function")