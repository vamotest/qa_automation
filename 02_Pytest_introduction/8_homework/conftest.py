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
def string_replace_data():
    str_for_replace = "1213141516171819101"
    return str_for_replace


@pytest.fixture()
def list_data():
    matrix = [[4, -5, 7], [1, -4, 9], [-4, 0, 5]]
    return matrix


@pytest.fixture()
def list_pairs_data():
    list1 = [2, 4, -5, 6, 8, -2]
    list2 = [2, -6, 8, 3, 5, -2]
    return list1, list2


@pytest.fixture()
def set_data():
    set1 = {1, 3, 5}
    set2 = {7, 5, 2}
    return set1, set2


@pytest.fixture()
def dict_data():
    players = {
        'Carlsen': 2842,
        'Caruana': 2822,
        'Mamedyarov': 2801,
        'Ding': 2797,
        'Giri': 2780
    }
    return players

