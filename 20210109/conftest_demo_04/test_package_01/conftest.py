import pytest

@pytest.fixture(name='test_package_01')
def setUp():
    print('test_package_01 start')
    yield
    print('test_package_01 ends')