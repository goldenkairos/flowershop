#WAVE 1
create a class called FlowerShop. This FlowerShop will contain an attribute, inventory, which will be a list of Flowers. The FlowerShop will have 2 class methods: refill_inventory and create_boquet.

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

#WAVE 2

Add an attribute to Flowers, called cost. Optional: Change your Flower initializer to use a default cost of 10.
Add a class method to Boquet, called get_cost. This method will return the sum of the cost of the flowers in the Boquet.
Update the main method to also print out the total cost of your boquet
Optional: override Flower's _str_ method so it prints nicely, eg "blue tulip"

 Make a couple of additional changes:
Let's have the flower's type include only their species name, like "tulip", instead of also containing the color. For example, this line should be red_rose = Flower("rose", "red")
Let's rework the refill_inventory method to make better use of your ideas:
I really like that you used a dictionary to keep track of your inventory via default_dict! It makes a lot of sense to use the system of flower->count and I think you should expand upon your great idea! I'll break it down into a few smaller pieces to help you see your plan all the way through:
A) Change your default_inventory to be exactly like the default_dict (copy/paste works!)
B) Now you can delete the old default_dict and just use the new, dictionary form of default_inventory
C) Adjust your refill_inventory logic to make more efficient use of your two dictionaries (default_inventory and self.inventory). 


##Minh's note (10/16)

1) self.inventory = default_dictionary. If we modify the self.dictionary, does that mean we also modify the default_dictionary as well? My assumption is no as theFlowerShop is an instance of Flower so they (self.inventory vs. default_dictionary) should have 2 different ids
2) create_bouquet method: what function to allow us randomly choose the key base on the number of value? My approach is to creating an additional list with key*value but I run into ValueError on * operator)