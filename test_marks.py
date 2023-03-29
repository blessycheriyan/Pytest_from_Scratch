import pytest
import sys

@pytest.mark.skip
def test_login():
    print('Login to the test server')
    
@pytest.mark.skipif(sys.version_info<(3,8),reason ="Python version is not supported")
def test_checkout():
    print('Checkout to Application')
    
@pytest.mark.xfail  
def test_logout():
    assert False
    print('Logout from Application')        
    
def test_close():
    assert True
    print('close Application')        