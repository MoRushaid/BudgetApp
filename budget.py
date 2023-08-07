class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = []
    
  def deposit(self, amount, description = ''):
    self.ledger.append({'amount' : amount, 'description' : description})

  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      self.ledger.append({'amount' : -1*amount, 'description' : description})
      return True
    else:
      return False

  def get_balance(self):
    funds = 0
    for entry in self.ledger:
        amount = entry.get('amount', 0)
        funds += amount
    return funds
    
  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    else:
      return True

  def transfer(self, amount, destination):
    if self.check_funds(amount):
      description = 'Transfer to ' + destination.category
      self.withdraw(amount, description)
      description = 'Transfer from ' + self.category
      destination.deposit(amount, description)
      return True
    else:
      return False

  def __str__(self):
    title = f"{self.category.center(30, '*')}"
    item_lines = [f"{item['description'][:23].ljust(23)}{item['amount']:>7.2f}" for item in self.ledger]
    items = "\n".join(item_lines)
    total = f"{'Total:'}{self.get_balance():>7.2f}"
    out = title + '\n' + items + '\n' + total
    return out
     
def create_spend_chart(categories):

  def formulate_x(categories, max_len):
    
    seperator = '    ' + ('---' * len(categories)) + '-'
    x_axis = seperator + '\n     '
    for i in range(max_len):
      for j in range(len(category)):
        try:
          x_axis += category[j][i] + '  '
        except:
          x_axis += '   '
      if i < max_len - 1:
        x_axis += '\n     '
    return x_axis 

  def formulate_y_values(ledgers):
    
    spent_by_category = []
    for entries in ledgers:
      ind_tot = 0
      for entry in entries:
        if entry['amount'] < 0:
          ind_tot += abs(entry['amount'])
      spent_by_category.append(ind_tot)
    
    
    tot = sum(spent_by_category)
    ind_percent = []
    
    for spent in spent_by_category:
      per = round(spent*100 // tot)
      if per < 10:
        per = 0
      else:
        per = round(per, -1)
      
      ind_percent.append(per)
  
    return ind_percent

  def formulate_y(total, y_axis):
      
    for i in range(len(y_axis)):
      y_axis[i] = y_axis[i] + total[i]
      
    return y_axis
  
  category = []
  max_len = 0
  ledgers = []
  for item in categories:
    category.append(list(item.category))
    ledgers.append(item.ledger)
    max_len = max(max_len, len(list(item.category)))

  y_axis = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
  
  x_axis = formulate_x(categories, max_len)
  
  percentages = formulate_y_values(ledgers)
  
  for percent in percentages:
    no_of_points = percent / 10
    row = []
    while no_of_points >= 0:
      row.append(' o ')
      no_of_points -= 1
    remaining = 11 - len(row)
    empty = ['   '] * remaining
    total = empty + row
    y_axis = formulate_y(total, y_axis)

  y_axis_str = ''
  for i in range(len(y_axis)):
    y_axis[i] += ' '
    if i < len(y_axis) - 1:
      y_axis[i] += '\n'  

  y_axis_str = ''.join(y_axis)
  out = 'Percentage spent by category\n' + y_axis_str + '\n' + x_axis
  return out
  
