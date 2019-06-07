
username = input("Please enter your user name")
password = input("Please enter your password")

# username = "venki"
# password = "venki@123"

users = ["venki", "rathod", "admin"]
passd = ["venki@123"]

if username in users and password in passd:
    print("You are a valid user")
else:
    print("your are not a valid user")