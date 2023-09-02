class Shoe:
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic SK8-Hi"
        self.price = 69.99
        self.in_stock = True
        
# Creating Instances of Shoe
skater_shoe = Shoe()
dress_shoe = Shoe()
print(skater_shoe.type)
print(dress_shoe.type)

# Setting values for the instance's attributes: 
print(" ")
skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)

# Passing in arguments to the __init__ method:
class Shoe2:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True # default set to True
        
print(" ")
runner_shoes = Shoe2("Nike", "Sprint Trainers", 89.99)
hiking_boots = Shoe2("Hiking Brand", "Mountain Climbers", 120.95)
print(runner_shoes.type)
print(hiking_boots.type)
