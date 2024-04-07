#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0, total=0 ):
    self.discount = discount
    self.total = total
    self.items = []
    self.price = []
    self.quantity = 0

  def add_item(self, title, price, quantity=1):
    self.total += float(price) * quantity
    self.quantity = quantity
    for i in range(quantity):
      self.items.append(title)
      self.price.append(price)
    return self.items
  
  def void_last_transaction(self):
    # breakpoint()
    if len(self.price) > 0:
      last_item_price = float(self.price[-1] * self.quantity)
      self.total -= last_item_price
      for i in range(self.quantity):
        self.price.pop(-1)
    else:
      self.total = 0.0




  def apply_discount(self):
    if self.discount > 0:
      discounted = self.total * (self.discount / 100)
      self.total -= discounted
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print("There is no discount to apply.")
  
