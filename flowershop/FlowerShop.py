from flowershop.Flower import Flower
import random
from flowershop.Boquet import Boquet

class FlowerShop:
    def __init__(self):
        self.inventory = default_inventory
        # {red_rose:2,
        #         white_rose:2,
        #         yellow_sunflower:2,
        #         yellow_tulip:2,
        #         blue_tulip:2 }

    # def refill_inventory(self):
    #     while len(default_inventory) < 10:
    #         for flower in default_inventory:
    #             print("debugging here",default_inventory[flower])
    #             count = self.inventory.count(flower)
    #             diff = default_inventory[flower] - count
    #             if diff != 0:
    #                 self.inventory.append(flower)
    #                 # print(default_inventory)
    
    def refill_inventory(self):
        while sum(self.inventory.values()) < sum(default_inventory.values()):
            for flower in default_inventory:
                if flower not in self.inventory:
                    self.inventory[flower] = default_inventory[flower]
                elif self.inventory[flower] < default_inventory[flower]:
                    self.inventory[flower] = default_inventory[flower]

    
    def create_boquet(self,number_of_flowers):
        flower_list = [red_rose, red_rose, white_rose, white_rose,yellow_sunflower,yellow_sunflower,yellow_tulip,yellow_tulip]
        # flower_list = [key*value for key,value in default_inventory.items()]
        selected_flowers = (random.sample(flower_list,number_of_flowers))
        # print("list of randomly chosen flowers are",selected_flowers)
        myboquet = Boquet()
        for flower in selected_flowers:
            myboquet.contents.append(flower)
            self.inventory[flower] = self.inventory[flower] - 1
        return myboquet

        

red_rose = Flower("rose","red")
white_rose = Flower("rose","white")
yellow_sunflower = Flower("sunflower","yellow")
yellow_tulip = Flower("tulip", "yellow")
blue_tulip =Flower("tulip", "blue")


default_inventory = {red_rose:2,
                white_rose:2,
                yellow_sunflower:2,
                yellow_tulip:2,
                blue_tulip:2 }


