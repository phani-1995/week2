class Stocks:
    def __init__(self,name,price,number):
        self.name = name
        self.price = price
        self.number = number
#This class contains portfolio of methods
class portfolio:
    def __init__(self):
        self.value=0
        self.portfolio=[]
    def enter_stock(self,name,price,number):
        new_stock=Stocks(name,price,number)
        self.portfolio.append(new_stock)
    def portfolio_details(self):
        # This method calculates total value of stock
        for obj in self.portfolio:
            print(f"{obj.name}:\n\tPrice per share: {obj.price}\n\t"
                  f"Number of Shares: {obj.number}\n\tValue: {obj.price * obj.number}\n.")
    def portfolio_total(self):
        #This method iterates through a portfolio and calculates total stock value
        for obj in self.portfolio:
            self.value += obj.number * obj.price

port=portfolio()
port.enter_stock("Microsoft", 1000000, 550)
port.enter_stock("Lufthansa", 5000000,600)
port.enter_stock("TCS", 1200000,1000)
port.portfolio_details()
port.portfolio_total()
print("Total portfolio value: ",port.value)





