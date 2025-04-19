# class Money:
#  def __init__(self, amount, currency):
#  self.amount = amount
#  self.currency = currency
#
#  def __add__(self, other):
#  if self.currency == other.currency:
#  return Money(self.amount + other.amount, self.currency)
#
#  def __str__(self):
#  return f"{self.amount} {self.currency}"
#
#
# m1 = Money(100, "eur")
# m2 = Money(230, "eur")
# print(m1 + m2)