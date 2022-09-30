class Category:

    def __init__(self,category):
        self.category=category
        self.ledger=[]

    def deposit(self,amount,description=""):
        aux={}
        aux["amount"]=amount
        aux["description"]=description
        self.ledger.append(aux)

    def get_balance(self):
        balance=0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def check_amount(self, amount):
        if amount > self.get_balance():
            return True
        return False

    def withdraw(self,amount,description=""):
        if self.check_amount(amount):
            aux={}
            aux["amount"]=0-amount
            aux["description"]=description
            self.ledger.append(aux)
            return True
        return False

    def transfer(self,amount,category):
        if self.check_amount(amount):
            self.withdraw(amount,description="Transfer to "+str(category))
            self.deposit(amount, description="Transfer from "+str(category))
            return True
        return False

    def __str__(self):
        s = self.category.center(30, "*") + "\n"

        for item in self.ledger:
            aux = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            s += aux + "\n"
        s += "Total: " + str(self.get_balance())
        return s

def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].category[i] + " "
      else:
        s += "   "
    s += " "

  return s
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(create_spend_chart([food, clothing]))