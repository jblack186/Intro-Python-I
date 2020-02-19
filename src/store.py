from category import Category

class Store:
    def __init__(self, name, categories=["toys", "food"]):
    # self.attribute = parameter
        self.name = name
        self.categories = categories

    def __str__(self):
        # return self.name
        output = f'Welcome to {self.name}'
        i = 1
        for cat in self.categories:
            output += f'\n{i}. + {cat.name}'
            i += 1
        return output 

my_store = Store("Pets Unlimited", [Category("Toys", ["chew toys", "cat nip", "ball"]),
                                    Category("Fish"),
                                    Category("Bedding/Cages"),
                                    Category("Food") ] )


print(my_store)
choice = int(input("Please choose a category (#): "))
print(choice)

#Should add error handling to input parser
# ex non integeger, ints outside of (0-size of categories)

while choice != 0:
    print(my_store.categories[choice-1])
    print(my_store)
    choice = int(input("Please choose a category (#): "))


print("Thanks for stopping by")