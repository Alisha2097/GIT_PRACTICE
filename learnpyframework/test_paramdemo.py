
import pytest

#parametrizing fixture 
@pytest.fixture(params = ["a","b"])
def demo_fixture(request):
    print(request.param)

def testLogout(demo_fixture):
    print("Logout Successful")

#mark parametrize
@pytest.mark.parametrize("a, b, final",[(2,6,8),(5,8,15),(5,10,15)])
def testadd(a, b, final):
    assert a+b == final 

