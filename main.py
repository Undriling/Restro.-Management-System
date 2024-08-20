from tkinter.messagebox import YESNO


menu={
    'Pizza': 40,
    'Burger': 50,
    'Hot-dog': 80,
    'Chicken-momo': 65,
    'Chicken-fried-rice': 110,
}
print("Welcome to My restro")
print("Pizza: 40\n Burger: 50\n Hot-dog: 80\n Chicken-momo: 65\n Chicken-fried-rice: 110\n")
# print(menu)
# item_no=int(input("How much item you wants to add: "))
order_total=0

total = int(input('Enter total number of items you want to buy: '))

for i in range(total):
    item=input("Enter your next item: ")
    item = item.capitalize()
    print(item)
    if item not in menu :
        print('Item is not available')
        break
    order_total +=menu[item]

another_item=input("Do you wants to add more item ? (Yes/No)")
if another_item=="Yes":
    total2= int(input('Enter total number of items you want to buy: '))
    for i in range(total2):
        item2=input("Enter your next item: ")
        item2= item2.capitalize()
        print(item2)
        if item2 not in menu :
            print('Item is not available')
            break    
        order_total +=menu[item2]
        print("Total payable amount: ", order_total)
else:
    # order_total +=menu[item2]
    print("Total payable amount: ", order_total)

    



# else:
#     print("Iten is currently not available")
# else:
#     print("Item is currently not available")
    
# for menu[item] in range(item_no):
#     print("Added your item in your cart: ")
#     order_total +=menu[item]
# else:
#     print("Item is currently not available")