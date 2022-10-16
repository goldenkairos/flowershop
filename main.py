from flowershop.Flower import Flower
from flowershop.FlowerShop import FlowerShop
from flowershop.Boquet import Boquet

def get_list(bouquet):
    flower_contents = []
    for flower in bouquet.contents:
        flower_contents.append(flower.__str__())
    return flower_contents

TheFlowerShop = FlowerShop()
# print("Initial number of flowers in the inventory is",len(TheFlowerShop.inventory))
# print("list of initial flowers",TheFlowerShop.inventory)

mybouquet = TheFlowerShop.create_boquet(5)
print("Inventory after creating a new instance of bouquet is",len(TheFlowerShop.inventory))
# print("List of remaining flowers in inventory is ", (TheFlowerShop.inventory))
print("The size of my bouquet is",mybouquet.get_size())
print("List of flowers in my bouquet:", get_list(mybouquet))

TheFlowerShop.refill_inventory()
print("Size of inventory after refill method",len(TheFlowerShop.inventory))


mybouquet.get_cost()




