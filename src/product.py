'''//string vs repr how to dsiiplay for users for developers
# repr for developersand infor theyd find userful

# __STR__ for users and info theyd find useful
'''

class Product:
def __init__(self,name,desriptioion,price=0):
    self.name
self.description=descriptionself.price = price
def __str__(self):
return f'{self.name} is ${self.price}'