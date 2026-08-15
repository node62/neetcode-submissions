class Account:
    def __init__(self, t, b):
        self.title = t
        self._balance = b
    
    def display_balance(self) -> None:
        print('Balance: $', self._balance, sep='')

# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
