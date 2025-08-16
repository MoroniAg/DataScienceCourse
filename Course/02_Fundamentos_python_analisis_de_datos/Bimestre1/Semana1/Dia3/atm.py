amount = 100
value = int(input("Enter the amount to withdraw: "))

if value > amount:
    print("Insufficient funds")
    exit()

if value % 10 != 0:
    print("Incorrect amount")
    exit()
    
print("Withdrawal successful")