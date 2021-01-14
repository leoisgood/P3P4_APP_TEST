import pytest

@pytest.fixture(name='main_package')
def setUp():
    print('main_package start')
    yield
    print('main_package ends')