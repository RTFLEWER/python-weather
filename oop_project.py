from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Dave.deposit(1000)
Sara.deposit(2000)

Dave.withdraw(6000)
Sara.withdraw(1000)

Dave.transfer(600, Sara)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(6000, Sara)
Blaze.transfer(1000, Sara)
