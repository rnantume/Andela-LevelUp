
""" Modeling a signup form for Uber riders using object oriented concepts"""

import re

users = []

class User:
    def __init__(self, first_name, last_name, phone_number, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = User.validate_email(email)
        self.password = password
    
    def save_on_submit(self, first_name, last_name, phone_number, email, password):
        user = {'fname': self.first_name,
                'lname': self.last_name,
                'contact_no':self.phone_number,
                'email': self.email,
                'password': self.password
                }
        users.append(user)
        return users
    
    @staticmethod
    def validate_email(email):
        regex = 
        if re.search(regex, email)
            return email      
        else:
            print("The email pattern does not match the standard!")


    def greeting(self):
        return("Hi {} {}!".format(self.first_name, self.last_name))

    
    def login(self, user_email, user_password):
        for u in users:
            if user_email ==  u.email and user_password == u.password:
                return("You have successfully logged in!")
            else: 
                return("Wrong credentils!")

# creating a rider1 object
rider1 = User("Tom", "Kagi", "0750112791", "nnrobin37@gmail.com", "wentoride123.")

# retrieving the object's email value
print(rider1.email) 

#calling the greeting function
print(rider1.greeting()) 

# saving the signup details
print(rider1.save_on_submit("Tom", "Kagi", "0750112791", "nnrobin37@gmail.com", "wentoride123."))

# logging in the rider
print(rider1.login("nnrobin37@gmail.com", "wentoride123.")) 

