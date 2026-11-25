
#Create a custom exception
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass



class BankAccount:
    def __init__(self, balance: float = 0):
        self.balance = balance

 
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Tried to withdraw {amount}, but balance is {self.balance}"
            )

        self.balance -= amount


account = BankAccount(50)


try:
    account.withdraw(30)
    print("Withdrawal successful!")

except InsufficientFundsError as err:
    print(err)


print("Remaining balance:", account.balance)
