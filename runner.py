from knapsacker import Knapsacker
class Item:
  def __init__(self, value, cost):
    self.value = value
    self.cost = cost

items = [Item(1, 4), Item(3, 2)]
for i in Knapsacker(items, capacity=4).pack():
  print(i.value)
