import random
password_length= int(input("Enter the length of the password:"))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!~@#$%^&*()_+?/;:"
password= "".join(random.sample(characters, password_length))
print(password)