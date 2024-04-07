class ShoppingCart:
    def __init__(self): 
        self.items = []

    def add_item(self,item_name, qty):
        item_name=input()
        qty=input()
        item = (item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):
        for item in self.items:     
            if item[0] == item_name:
                self.items.remove(item)
            break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    
cart = ShoppingCart()
print("enter the elements to add")
elements = input()
cart.add_item(item_name)
# cart.add_item("fruites",25)
# cart.add_item("veg",50)
print(cart.items)
print("Products in cart is:")
for item in cart.items:
    print(item[0],"=",item[1])
total_qty = cart.calculate_total()
print("Total cart value is: ",total_qty)

print("Type the item to delete")
s = input()
cart.remove_item(s)
print("Products in cart after remove is:")
for item in cart.items:
    print(item[0],"=",item[1])
total_qty = cart.calculate_total()
print("Total final cart value is: ",total_qty)




