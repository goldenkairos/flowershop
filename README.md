Let's have you create a class called FlowerShop. This FlowerShop will contain an attribute, inventory, which will be a list of Flowers. The FlowerShop will have 2 class methods: refill_inventory and create_boquet.

refill_inventory will take no parameters and it will not return anything. This method will check the existing inventory and check if it has 2 of each Flower type in each color (I'll write more about the flowers/colors later). If any flowers are missing, they are added back to the  inventory.

create_boquet will take one parameter, number_of_flowers, and it will return a Boquet (more on this later). The Boquet will consist of the designated number of flowers which will be taken randomly from the FlowerShop's inventory.

The Boquet class will have one attribute, contents, which will be a list containing all of the flowers in the boquet. It will also have a class method, get_size, that will return how many flowers are in the boquet.

The Flower class will have 2 attributes, type and color. The Flower constructor (__init__) should require both type and color to be passed as arguments.

The default inventory should have the following flowers:
2 red roses
2 white roses
2 yellow sunflowers
2 yellow tulips
2 blue tulips

Your main method will do the following:
 - Create a new instance of FlowerShop.
 - Print the FlowerShop's inventory
 - Call the FlowerShop's refill_inventory method
 - Print the FlowerShop's inventory
 - Call the FlowerShop's create_boquet method with a number_of_flowers argument of 5.
 - Print the FlowerShop's inventory
 - Print the Boquet returned by the create_boquet call
