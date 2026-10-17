
print("========================================")
print("       BANK ACCOUNT SIMULATOR")
print("========================================")

balance = 0.0
transactions = []


def check_balance():
    print(f"\nCurrent balance: Rs. {balance:.2f}")


def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount (Rs.): "))

        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return

        balance += amount
        transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": balance
        })

        print(f"Rs. {amount:.2f} deposited successfully.")
        check_balance()

    except ValueError:
        print("Error: Please enter a valid amount.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount (Rs.): "))

        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Error: Insufficient balance.")
        else:
            balance -= amount
            transactions.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": balance
            })

            print(f"Rs. {amount:.2f} withdrawn successfully.")
            check_balance()

    except ValueError:
        print("Error: Please enter a valid amount.")


def show_transactions():
    if not transactions:
        print("\nNo transactions available.")
        return

    print("\n========== TRANSACTION HISTORY ==========")
    print(f"{'Type':<15}{'Amount (Rs.)':>15}{'Balance (Rs.)':>17}")
    print("-" * 47)

    for transaction in transactions:
        print(
            f"{transaction['type']:<15}"
            f"{transaction['amount']:>15.2f}"
            f"{transaction['balance']:>17.2f}"
        )

    print("=" * 47)


while True:
    print("\n========== MAIN MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")
    print("===============================")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        show_transactions()
    elif choice == "5":
        print("\nThank you for using the Bank Account Simulator!")
        check_balance()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select between 1 and 5.")
