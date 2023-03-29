
from turtle import title


def test_1():
    x =2 + 2
    y =4
    assert x == y
       
def test_2():
    name = 'Selenium'
    title = 'Selenium is for web automation tool' 
    assert name  in title
    
def test_3():
    name= 'Jenkins'
    title ='Jenkins is CI server'    
    assert name in title, 'Title does not match'