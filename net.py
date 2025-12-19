class NetBankingUser:
    def __init__(self, username, daily_limit=5000):
        self.username = username
        self.daily_limit = daily_limit
        self.daily_spent = 0

    def set_daily_limit(self, new_limit):
        """Allow user to set their own daily transaction limit"""
        self.daily_limit = new_limit
        print(f"Daily limit updated to ₹{new_limit} for {self.username}")

    def make_transaction(self, amount):
        """Process a transaction if within daily limit"""
        if self.daily_spent + amount > self.daily_limit:
            print(f"Transaction denied! Daily limit of ₹{self.daily_limit} exceeded.")
            return False
        else:
            self.daily_spent += amount
            print(f"Transaction of ₹{amount} successful. Total spent today: ₹{self.daily_spent}")
            return True

    def reset_daily_spent(self):
        """Reset daily spent at midnight (simulate new day)"""
        self.daily_spent = 0
        print(f"Daily spent reset for {self.username}")


# 🔹 Interactive usage
username = input("Enter your username: ")
initial_limit = int(input("Set your initial daily limit (₹): "))

user = NetBankingUser(username, daily_limit=initial_limit)

while True:
    print("\nOptions:")
    print("1. Make a transaction")
    print("2. Update daily limit")
    print("3. Reset daily spent (new day)")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = int(input("Enter transaction amount (₹): "))
        user.make_transaction(amount)

    elif choice == "2":
        new_limit = int(input("Enter new daily limit (₹): "))
        user.set_daily_limit(new_limit)

    elif choice == "3":
        user.reset_daily_spent()

    elif choice == "4":
        print("Exiting NetBanking system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
