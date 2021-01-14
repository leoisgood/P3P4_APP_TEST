import pytest

@pytest.fixture(name='test_package_02')
def setUp():
    print('main_package start')
    yield
    print('main_package ends')