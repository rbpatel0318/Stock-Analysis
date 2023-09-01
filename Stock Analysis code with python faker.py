import string
import random
from faker import Faker
from faker.providers import BaseProvider

class Stock_Data_Analysis(BaseProvider):

    def stock_symbol(self):
        letters = string.ascii_uppercase
        return ''.join(random.choices(string.ascii_uppercase, k=4))
    
    def stock_price(self):
        return round(random.uniform(100,2000),2)
    
    def stock_volume(self):
        return random.randint(100000,2000000)
    
    def stock_valuation(self):
        price = round(random.uniform(100,2000),2)
        volume = random.randint(100000,2000000)
        return round(price * volume)
    
    def stock_price_max(self):
        return round(random.uniform(100,2000),2)
    
    def stock_price_min(self):
        return round(random.uniform(10,1000),2)
    
    def stock_eps(self):
        netincome = round(random.uniform(100000,2000000),10)
        outstandingshares = random.randint(10000,2000000)
        return round(netincome / outstandingshares)
    
    def stock_dividend(self):
        return round(random.uniform(0.5,10))
    
if __name__ == '__main__':
    Stock_Data_Analysis_object = Stock_Data_Analysis(BaseProvider)
    faker = Faker()
    print("Company Stock Symbol:",Stock_Data_Analysis_object.stock_symbol())
    print("Stock Price: $",Stock_Data_Analysis_object.stock_price())
    print("Company Stock Volume: $",Stock_Data_Analysis_object.stock_volume())
    print("Stock Valuation: $",Stock_Data_Analysis_object.stock_valuation())
    print("Max Price: $",Stock_Data_Analysis_object.stock_price_max())
    print("Min Price: $",Stock_Data_Analysis_object.stock_price_min())
    print("Eps: $",Stock_Data_Analysis_object.stock_eps())
    print("Yearly Dividend: $",Stock_Data_Analysis_object.stock_dividend())
    print("      Rudra Patel Stock Analysis Internship - Brandon Consulting Associates / Inteliclear LLC    ")