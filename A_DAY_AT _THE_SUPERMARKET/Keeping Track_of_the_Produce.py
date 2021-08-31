#In this code we track the how much stock we have and how much sell.
#Eg for food in XXXXX:
#" %s" % prices[food]
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print(food)
  print("price: %s" % prices[food])
  print("stock: %s" % stock[food])