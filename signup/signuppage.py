import re
import uuid

users = []
class User:
    
    def __init__(self):
        self.details = {}
        
    def save_details(self, first_name, last_name, phone_number, email, password):
        try:
            self.details[id] = uuid.uuid4().int
            self.details[first_name] = input("Enter your first name: ")
            self.details[last_name] = input("Enter your last name: ")
            self.details[phone_number] =input("Enter your phone number: ")
            self.details[email] = input("Enter your email: ")
            self.details[password] = input("Enter a password")        
        except AttributeError:
           raise("All fields must be filled!")
        else:
            return users.append(self.details)

    @staticmethod
    def validate_email(email):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) == 1:
            return email      
        else:
            print("The email pattern does not match the standard!")

    def greeting(self, id):
        for user in users:
            if user[id] == id:
                return("Hi {} {}!".format(user[first_name], user[last_name])
 
    def find_rider(self, user_id):
        for user in users: 
            if user[id] == user_id:
                return user
            
        return("Person of id {} not found".format(id))

    def login(self, user_email, user_password):
        for user in users:
            if user_email ==  user[email] and user_password == user[password]:
                return("You have successfully logged in!")
            else: 
                return("Wrong credentils!")

print("="*40)

# creating a rider1 object
rider1 = User()

# saving the signup details
print(rider1.save_details()

#calling the greeting function
print(rider1.greeting(input"Enter user id: "))  

# find rider
print(rider1.find_rider("Enter rider ID: "))

# let's login the user
print(rider1.login(input("Enter email address: "), input("Enter your password: ")))