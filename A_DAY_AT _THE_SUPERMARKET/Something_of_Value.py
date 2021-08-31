prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

#In this code we check how much profit we get from stock and sell.
total = 0
for food in prices:
  print(prices[food] * stock[food])
  total = total + prices[food] * stock[food]
print(total)