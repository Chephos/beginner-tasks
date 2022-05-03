# Mock USSD service
import sys
ussd = input("Enter your ussd code: ")
pwd = "30doCode"

# 1. "Check balance"
# 2. "Send money"
# 3. "Purchase"
# 4. "Purchase airtime"
account_balance = 1_000_503
def check_balance():
    global account_balance
    password  = input("Enter your Password: ")
    count = 0
    if password ==pwd:
        return print(f"Your account balance is ${account_balance}")
    else:
        print("Incorrect Password!")
        count += 1
        if count <= 5:
            check_balance()
        # TODO: How to exit the program
        else:
            exit()



def send_money():
    global account_balance
    print('Select a bank.')
    print("1. GT Bank\n2. Access Bank\n3. Fidelity Bank\n4. Wema Bank\n5. Union Bank\n6. Polaris Bank\n7. Globus Bank\n8. Keystone Bank")
    bank = input("---> ")
    acct_num = int(input('Account Number of receiver: '))
    amount = int(input("Enter amount: $"))
    password = input("Enter your password: ")
    if password == pwd:
        account_balance -= amount
        return print(f"{amount} has been sent.\nYour account balance is ${account_balance}")

#send_money()
check_balance()

