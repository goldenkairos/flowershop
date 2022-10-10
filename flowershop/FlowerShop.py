from flowershop.Flower import Flower
import random

class FlowerShop:
    def __init__(self):
        self.inventory = default_inventory

    def refill_inventory(self):
        default_dict = {red_rose:2,
                     white_rose:2,
                     yellow_sunflower:2,
                     yellow_tulip:2,
                     blue_tulip:2, }

        while len(default_inventory) < 10:
            for flower in default_dict:
                count = self.inventory.count(flower)
                diff = 2 - count
                if diff != 0:
                    self.inventory.append(flower)
                    print(default_inventory)

    
    def create_boquet(self,number_of_flowers):
        boquet = [random.sample(self.inventory,number_of_flowers)]
        return boquet
        

red_rose = Flower("redrose","red")
white_rose = Flower("whiterose","white")
yellow_sunflower = Flower("yellowsunflower","yellow")
yellow_tulip = Flower("yellowtulip", "yellow")
blue_tulip =Flower("bluetulip", "blue")

default_inventory = [red_rose,red_rose,
                     white_rose,white_rose,
                     yellow_sunflower,yellow_sunflower,
                     yellow_tulip, yellow_tulip,
                     blue_tulip, blue_tulip
                     ]


