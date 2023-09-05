class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price =  price
        self.stock = True

    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent) 

skater_shoe  = Shoe("Vans", "Low-top", 59.99)
dress_shoe = Shoe("Jack Jill", "Ballet Flats", 29.99)

# Skater shoes go on sale for 20% off
# skater_shoe.price   =  skater_shoe.price * (1 - 0.2)

# Dress shoes go on sale 10% off
# dress_shoe.price = dress_shoe.price * (1 - 0.1)

# skater shoe goes again on sale for another 10%:
# skater_shoe.price = skater_shoe.price * (1 - 0.1)

# Test on_sale_by_percent method
skater_shoe.on_sale_by_percent(0.2)
print(skater_shoe.price)

dress_shoe.on_sale_by_percent(0.5)
print(dress_shoe.price) 