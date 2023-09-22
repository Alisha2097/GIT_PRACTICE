import pytest

@pytest.fixture(scope ="session",autouse=True) 
# @pytest.fixture(scope ="function",autouse=True) 
# @pytest.fixture(scope ="class",autouse=True) 
# @pytest.fixture(scope ="module",autouse=True) 
# @pytest.fixture(scope ="package",autouse=True) 
# def tc_setup(): #setup methods = precondtions
#     print("Launch browser")
#     print("Login")
#     print("Browse products")
#     yield #teardown
#     print("Logoff")
#     print("Close browser")

def tc_setup(browser): #setup methods = precondtions
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "ff":
        print("Launch Firefox")
    else:
        print("provide valid browser")

    print("Login")
    print("Browse products")
    yield #teardown
    print("Logoff")
    print("Close browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope ="session",autouse=True)
def browser(request):
    return request.config.getoption("--browser")