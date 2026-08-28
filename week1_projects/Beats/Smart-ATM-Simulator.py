"""
step1:-print the first message "===== NeuroByte ATM ====="
step2:- make a dictanary of customers in which has each each customer data like Name ,Balance , Pin_code
step3:-Take input from user for  pin code
step4:-Check if the pin code is correct and if not use while loop and ask again.
step5:-If the pin code is correct, display ===== ATM MENU =====
step6:-Take input from user what user want to do
step7:-if user want to desposit then add the balance
step8:-if user want to withdraw then subtract the balance
step9:-if user want to check balance then display the balance
step10:-if user want to exit then print "Have a nice day, sir!"
"""

print("===== NeuroByte ATM =====")
customers = {
    1:{"Name":"Saksham", "Balance":312},
    2:{"Name":"Motor","Balance":200},
    3:{"Name":"Aaron","Balance":2280},
    4:{"Name":"thermocool","Balance":4500},
    5:{"Name":"Boomer","Balance":720},
    6:{"Name":"Gooner","Balance":23200},       
}

pin_code = int(input("Enter your pin code: "))

# Keep asking until the correct PIN is entered
while pin_code not in customers:
    print("Wrong PIN! Try again.")
    pin_code = int(input("Enter your pin code: "))

print("===== ATM MENU =====")

user_wants = input(
    "A. Check Balance\n"
    "B. Deposit Money\n"
    "C. Withdraw Money\n"
    "D. Exit\n"
    "Kindly give input (A, B, C, D): "
).upper()

if user_wants == "A":
    print(
        f"Hello {customers[pin_code]['Name']}\n"
        f"Your account balance is {customers[pin_code]['Balance']}"
    )

elif user_wants == "B":
    deposit_amount = int(input("Enter your amount: "))
    customers[pin_code]["Balance"] = customers[pin_code]["Balance"] + deposit_amount
    print("Money deposited successfully.")
    print(f"Your account balance is {customers[pin_code]['Balance']}")

elif user_wants == "C":
    withdraw_amount = int(input("Enter your amount: "))
    customers[pin_code]["Balance"] = customers[pin_code]["Balance"] + deposit_amount
    print("Money withdrawn successfully.")
    print(f"Your account balance is {customers[pin_code]['Balance']}")
    
elif user_wants == "D":
    print("Have a nice day, sir!")

else:
    print("Invalid option.")
