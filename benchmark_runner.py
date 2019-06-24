import sys
from datetime import datetime
from knapsacker import Knapsacker

class Item:
  def __init__(self, value, cost):
    self.value = value
    self.cost = cost

class Runner:
  def __init__(self, input, capacity=10):
    self.input = input
    self.capacity = int(capacity)

  def items(self):
    return [
      Item(int(v), int(c)) for [v, c] in [
        line.split() for line in self.input
      ]
    ]

  def load(self):
    self.knapsacker = Knapsacker(self.items(), self.capacity)

  def run(self):
    self.result = self.knapsacker.pack()

r = Runner(sys.stdin, sys.argv[1])
r.load()
before = datetime.now()
r.run()
after = datetime.now()
print(after - before)
if sys.argv[2] == "-v":
  print(str(len(r.result)) + " items: value " + str(sum([i.value for i in r.result])) + ", cost " + str(sum([i.cost for i in r.result])))
