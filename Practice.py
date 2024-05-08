# Простая учетная система
#Определить класс "Account", имитирующий банковский счет. Класс должен включать атрибуты для хранения идентификатора владельца,
#баланса счета и методы для депозита(пополнения) и снятия средств, если на счету достаточно средств.

class account:
    def __init__(self, id, balance=0):
        self.id = id #идентификатор владельца
        self.balance = balance #баланс счета

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Теперь ваш баланс составляет {self.balance}")
    def withdraw(self, money): #метод снятия средств
        if money > self.balance: #проверка на достаточность средств
            print("Недостаточно средств на счету")
        elif money <= self.balance:#если средств достаточно
            self.balance -= money #снимаем средства
            print(f"Вы успешно сняли средства. Теперь ваш баланс составляет {self.balance}")

    def all_balance(self):
        print(f"Ваш баланс составляет {self.balance}")


man = account(1, 600)
man.all_balance()
man.withdraw(450)
man.withdraw(600)
man.deposit(20000)



