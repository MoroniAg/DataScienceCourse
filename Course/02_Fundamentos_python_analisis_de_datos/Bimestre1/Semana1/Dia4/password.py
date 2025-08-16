secret = input("Enter your secret password: ")
password = '1234asd'

while True:
    if secret == password:
        print("Access granted")
        break
    else:
        print("Access denied")
        secret = input("Enter your secret password: ")
