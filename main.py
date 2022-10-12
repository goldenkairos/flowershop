from flowershop.Flower import Flower
from flowershop.FlowerShop import FlowerShop
from flowershop.Boquet import Boquet



TheFlowerShop = FlowerShop()
print("Initial number of flowers in the inventory is",len(TheFlowerShop.inventory))


mybouquet = TheFlowerShop.create_boquet(5)
print("Inventory after creating a new instance of bouquet is",len(TheFlowerShop.inventory))
print("The size of my bouquet is",mybouquet.get_size())

TheFlowerShop.refill_inventory()
print("Size of inventory after refill method",len(TheFlowerShop.inventory))