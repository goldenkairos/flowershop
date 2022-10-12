from flowershop.Flower import Flower
from flowershop.FlowerShop import FlowerShop
from flowershop.Boquet import Boquet



TheFlowerShop = FlowerShop()

print(len(TheFlowerShop.inventory))

TheFlowerShop.refill_inventory()

# print(len(TheFlowerShop.inventory))

mybouquet = TheFlowerShop.create_boquet(5)

# print(mybouquet)

# mybouquet = Boquet()

# print(mybouquet)