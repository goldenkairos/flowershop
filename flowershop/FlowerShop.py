from flowershop.Flower import Flower


class FlowerShop:
    def __init__(self):
        self.inventory = default_inventory

    def refill_inventory(self):
        default_dict = {red_rose:2,
                     white_rose:2,
                     yellow_sunflower:2,
                     yellow_tulip:2,
                     blue_tulip:2, }
        
        # counts = dict()
        list = []
        for flower in default_inventory:
            list.append(flower.color)
        print(list)
    
        for flower in default_dict:
            count = default_inventory.count(flower)
            diff = 0
            print(count)
            while diff != 0:
                if count == 2 :
                    self.inventory = self.inventory
                else:
                    self.inventory.append(flower)
                    # counter +=1
                # while count !=2 :
                #     self.inventory.append(flower)    
        
        list2 = []
        for flower in default_inventory:
            list2.append(flower.color)
        print(list2)


    
    
    
    
    def create_boquet(number_of_flowers):
        pass

red_rose = Flower("rose","red")
white_rose = Flower("rose","white")
yellow_sunflower = Flower("sunflower","yellow")
yellow_tulip = Flower("tulip", "yellow")
blue_tulip =Flower("tulips", "blue")

default_inventory = [red_rose,red_rose,
                     white_rose,
                    
                     yellow_tulip, yellow_tulip,
                     blue_tulip, blue_tulip
                     ]


