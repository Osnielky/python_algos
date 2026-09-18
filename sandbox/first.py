

def deposit():
    amount = input("Enter the amount to deposit: ")
    if amount.replace('.', '', 1).isdigit():
        amount = int(amount)
        return amount
    else:
        print("Invalid input. Please enter a numeric value.")
        return None

def main ():
    balance = deposit()
    print(f"Your current balance is: {balance}")

main()