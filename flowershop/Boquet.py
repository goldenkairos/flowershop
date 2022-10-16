from flowershop.Flower import Flower

class Boquet:
    def __init__(self):
        self.contents = []
        
    def get_size(self):
        return len(self.contents)
    
    def get_cost(self):
        total = 0
        for flower in self.contents:
            total += flower.cost
            # print("Flower",flower,"with cost is",flower.cost)
            # print("total is",total)
        print("Total cost of the bouquet is",total)