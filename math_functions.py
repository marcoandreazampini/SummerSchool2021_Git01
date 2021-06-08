import pytest

def sum(a,b):
  return a + b

def test_sum():
  assert sum(2,4) == 6 

  
  
def banafshedivide(a,b):
  return a / b

def multiMarco(a,b):
  return a**b

if __name__ == '__main__':
  a = sum(banafshedivide(multiMarco(3,4),6),10))
