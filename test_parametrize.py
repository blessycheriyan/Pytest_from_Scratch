import pytest
import sys

@pytest.mark.parametrize("username,password", 
                         [
                             ("Selenium","webdriver"),
                             ("Python","Pytest"),
                             ("Mary","Emmanuel"),
                        ]
                         )
def test_login(username,password):
    print(username)
    print(password)

