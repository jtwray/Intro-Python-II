class Store:
    def __init__(self,name,categories):
        self.name = name
        self.categories = categories
        
    def __str__(self):
        output=self.name

        i=1
        for cat in self.categories:
            output+= f'\n{i}. {cat}'
            i+=1
        output += f'\n{i}. Quit'

        return output

    def __repr__(self):
        return f'{self.name} has {len(self.categories)} categories'

# from category import Category

class Category:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'{self.name}'
        
my_store =Store("PetPlus", [Category("Food"),Category("Costumes"),Category("Toys")])

print(my_store)

selection = int(input('Please select a category number:\n'))-1

while(selection != len(my_store.categories)):
    if selection >=int(4):
       print('''
       🚫⛔invalid category selected⛔🚫-- 🙅🏻‍♀️ 
       🙊🙉🙈
       
       Try again next ⌛
       youQuit!👋🏻 BYe. ''')
       break
    
    print(f'You selected {my_store.categories[selection]}')
    selection= int(input('Please select a category number:\n'))-1
if selection== int(3):
       print('youQuit!BYe.')

    