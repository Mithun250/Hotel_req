class hotel:
  def __init__(self,data):
    self.menu_list=data
    self.orders={}

  def show(self):
    print("Menu:")
    for i, j in self.menu_list.items():
        print(f"{i}: {j:.2f}")

  def place_order(self,dish,quantity=1):
    if dish in self.menu_list:
        if dish in self.orders:
          self.orders[dish]+=quantity
        else:
          self.orders[dish]=quantity

        print("ordered",dish,quantity)
        return True
    else:
      print(dish,"is not available" )
      return False

  def remove_order(self,dish,quantity=1):
    if dish in self.orders:
      if self.orders[dish]<=quantity:
        del self.orders[dish]
      else:
        self.orders[dish]-=quantity
      
      print(dish,"has been removed sucessfully")
      return True
    else:
      print("Did not order",dish)
      return False


  def show_orders(self):
    if not self.orders:
      print("No order placed yet")
    else:
      print("Customer Orders are: ")
      for i,j in self.orders.items():
        print(i,j)

  def total_price(self):
    total_price=0.0
    for dish,quantity in self.orders.items():
      if dish in self.menu_list:
        total_price= total_price + self.menu_list[dish] * quantity
    return total_price




class customer:
  def __init__(self):
      self.order = {}

  def show_order(self):
    if not self.order:
      print("Mithun's Order is empty")
    else:
      print("Customer Orders are: ")
      for i,j in self.order.items():
        print(i,j)


  def show(self):
    print("Mithun's Order: ")
    for i,j in self.order.items():
      print(i,j)

  def order_items(self):
      print("Enter the dish you want to order:")
      self.dish = input()
      return self.dish

  def remove_dish(self):
    print("Enter the dish you want to remove:")
    self.dish=input()
    return self.dish

  def show_total(self,hotel):
    total_price=hotel.total_price()
    if total_price > 0:
      self.show_order()
      print(f"total amount is: {total_price:.2f}")




chen_hotel=hotel({"idly":10,"dosa":25,"vada":10,"poori":30,"coffee":15})
mithun=customer()

while True:

  print("------------------------------------------------------------------------")
  print("select the option bellow")
  print("1 - Show the items \n2 - Customer ordering a Food \n3 - Show the Orders \n4 - Remove the dish from order  \n5 - Show all orders for hotel \n6 - Show orders with total  \n0 - exit")
  option =int(input("Enter the number : "))
  print("------------------------------------------------------------------------")
  if option==1:
    chen_hotel.show()

  if option==2:
    dish=mithun.order_items()
    status=chen_hotel.place_order(dish)
    if status:
        if dish in mithun.order:
            mithun.order[dish] += 1
        else:
            mithun.order[dish] = 1

  if option==3:
    mithun.show()

  if option==4:
    dish=mithun.remove_dish()
    status=chen_hotel.remove_order(dish)
    if status:
      if dish in mithun.order:
        mithun.order[dish]-=1
        if mithun.order[dish]<=0:
          del mithun.order[dish]

  if option==5:
    chen_hotel.show_orders()

  if option==6:
    mithun.show_total(chen_hotel)


  if option ==0:
    break
