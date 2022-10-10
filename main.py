from flowershop.Flower import Flower
from flowershop.FlowerShop import FlowerShop




TheFlowerShop = FlowerShop()

print(len(TheFlowerShop.inventory))

TheFlowerShop.refill_inventory()

bouquet = TheFlowerShop.create_boquet(5)

print(bouquet)