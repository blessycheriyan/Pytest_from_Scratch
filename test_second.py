import pytest

@pytest.mark.smoke
def test_login():
    print('Login to Application')
    
@pytest.mark.regression    
def test_checkout():
    print('Checkout to Application')
    
@pytest.mark.smoke   
def test_logout():
    print('Logout from Application')        