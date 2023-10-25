class BankAccount:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance is ${self.balance}."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.balance}."
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def check_balance(self):
        return f"Account balance for {self.owner}: ${self.balance}"

    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.deposit(amount)
            return f"Transferred ${amount} to {other_account.owner}. New balance is ${self.balance}."
        else:
            return "Invalid transfer or insufficient funds."

# Example usage:
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(account1.check_balance())
print(account2.check_balance())

print(account1.deposit(200))
print(account1.check_balance())

print(account1.withdraw(300))
print(account1.check_balance())

print(account1.transfer(account2, 200))
print(account1.check_balance())
print(account2.check_balance())
