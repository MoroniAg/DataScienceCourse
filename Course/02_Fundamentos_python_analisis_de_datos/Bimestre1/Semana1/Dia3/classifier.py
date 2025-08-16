age = int(input("Enter your age: "))

if age < 12:
    print("Child")
elif 12 <= age <= 17:
    print("Teenager")
elif 18 <= age < 59:
    print("Adult")
else:
    print("Senior")

