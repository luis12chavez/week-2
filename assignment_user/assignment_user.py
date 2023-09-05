class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Methods(Functions) Here:\
    def display(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if(self.is_rewards_member == True):
            print(f"{self.first_name} is already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        
        return self

    def spend_points(self, amount):
        if (amount <= self.gold_card_points):
            self.gold_card_points = self.gold_card_points - amount
            print(f"Balance Left: {self.gold_card_points}")
        else:
            print("Not enough points!")
        
        return self


test_user = User("Joe", "Smith", "joe_smith@gmail.com", 43)
test_user.display()

# User will now be Enrolled, with 200 Gold Card points
test_user.enroll()
test_user.enroll() # Will give message that they are enrolled already
print(" ")


test_user.spend_points(25)
print(test_user.gold_card_points) # Will output: 175
test_user.spend_points(176)
print(" ")

# Chained Methods:
test_user2 = User("Jane", "DoLittle", "janeDoLittle@gmail.com", 37)
test_user2.spend_points(75).enroll().spend_points(75).enroll().display()