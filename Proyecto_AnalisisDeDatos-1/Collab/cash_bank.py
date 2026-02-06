# Cash Bank

usuario = (input("Enter your name: ")).capitalize()
contraseña = input("Enter your password (Save password): ")
balance = float(input("Enter your ammount of cash: "))

menu = """Options (Write the number to choose the option you want to do):
1→ Current Balance.
2→ Add to Balance.
3→ Withdraw Balance.
4→ Pay.
"""
print("")
user = (input("Enter the name linked to your bank account: ")).capitalize()
if user == usuario:
    password = input("Enter your password: ")
    if password == contraseña:
        print(f"""Welcome to your bank account {user}, what you want to do?
                  
{menu}""")
        validation = True
    else:
        print("Invalid password")
        validation = False
else: 
    print("Invalid username.")
    validation = False
    

if validation:
    option = int(input("Your choose: "))
    if option == 1:
        print(f"Your current balance is: {balance}")
    elif option == 2:
        add_balance = float(input("Amount to add: "))
        balance = balance + add_balance
        print(f"""Amount added to your balance.
              Your new balance: {balance}""")
    elif option == 3:
        withdraw_balance = float(input("Ammount to withdraw: "))
        if withdraw_balance > balance:
            print("Not enough cash to withdraw.")
        else:
            balance = balance - withdraw_balance
            print(f"""Balance succesfuly withdrawn.
Your new balance: {balance}""")
    elif option == 4:
        pay_ammount = float(input("Ammount to pay: "))
        if pay_ammount > balance:
            print("Not enough cash to pay.")
        else:
            balance = balance - pay_ammount
            print(f"""Succesfully Paid.
Your new balance: {balance}""")
    else:
        print("Wrong Option.")
else:
    print("Wrong Validation.")
print("...")