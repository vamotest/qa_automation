import pytest


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture()
def sum_integers_data():
    return 4, 5


@pytest.fixture()
def string_data():
    str_pal = "А роза упала на лапу Азора"
    return str_pal


@pytest.fixture()
def list_data():
    matrix = [[4, -5, 7], [1, -4, 9], [-4, 0, 5]]
    return matrix
