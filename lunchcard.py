# Soru için: part 8 > More examples of classes > LunchCard sorusu

# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_special(self):
        if self.balance - 4.6 < 0:
            return
        self.balance -= 4.6

    def eat_lunch(self):
        if self.balance - 2.6 < 0:
            return
        self.balance -= 2.6
    
    def deposit_money(self, deposit):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += deposit
    
def main(): 
    peters_card = LunchCard(20)
    graces_card = LunchCard(30)
    peters_card.eat_special()
    graces_card.eat_lunch()
    print("Peter:", peters_card)
    print("Grace:", graces_card)
    peters_card.deposit_money(20)
    graces_card.eat_special()
    print("Peter:", peters_card)
    print("Grace:", graces_card)
    peters_card.eat_lunch()
    peters_card.eat_lunch()
    graces_card.deposit_money(50)
    print("Peter:", peters_card)
    print("Grace:", graces_card)
    

if __name__ == "__main__":
    # 1,2,3
    # card = LunchCard(50)
    # print(card)

    # card.eat_lunch()
    # print(card)

    # card.eat_special()
    # card.eat_lunch()
    # print(card)

    # card.deposit_money(-10)
    # print(card)
    main()
