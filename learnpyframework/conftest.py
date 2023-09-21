import pytest

# @pytest.fixture(scope ="session",autouse=True) 
@pytest.fixture(scope ="function",autouse=True) 
# @pytest.fixture(scope ="class",autouse=True) 
# @pytest.fixture(scope ="module",autouse=True) 
# @pytest.fixture(scope ="package",autouse=True) 
def tc_setup(): #setup methods = precondtions
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield #teardown
    print("Logoff")
    print("Close browser")