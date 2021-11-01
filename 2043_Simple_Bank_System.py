class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # 1번 계좌에서 2번 계좌로 달러를 송금
        if account1 <= 0 or account1 > len(self.balance) or account2 <= 0 or account2 > len(self.balance):
            return False
        if self.balance[account1-1] >= money:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        else : return False

    def deposit(self, account: int, money: int) -> bool:
        # 계좌에 돈을 넣는다
        if account <= 0 or account > len(self.balance) :
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # 계좌에서 돈을 뺀다
        if account <= 0 or account > len(self.balance) :
            return False
        if self.balance[account-1] < money:
            return False
        else : 
            self.balance[account-1] -= money
            return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
