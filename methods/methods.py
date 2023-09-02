class User:
    # ! Constructor Function!!! Creates the instance of an Object
    def __init__(self, first_name, last_name, age):
        self.first_name =  first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello my name is {self.first_name}. Age: {self.age}")

test_user = User("Joe", "Smith", 84)
test_user.greeting()