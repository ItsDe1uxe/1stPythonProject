def printList(buylist):
    print(", ".join(buylist))

def printListAmount(buylist):   #Prints the amount of items on the list
    print("Amount of Items in list:", len(buylist))

def checkItem(buylist):     #Checks if the item is on the list
    is_item_in_list = input("Please Enter an Item you want to check: ")
    if buylist.count(is_item_in_list) >= 1:
        print("Item", is_item_in_list, "Is on the list.")
    else:   #If it isn't, print that it isn't on the list
        print("The Item", is_item_in_list, "Isn't on the list.")

def printQuantity(buylist):     #Prints the amount of times an item is on the list
    in_list = []
    item_times_in_list = input("Please enter the item you want to know the quantity of: ")
    print("The item", item_times_in_list , "is featured", buylist.count(item_times_in_list), "Times")

            
    
def deleteItem(buylist):    #Deletes an item from the list
    delete_item_from_list = input("Enter the name of the item you want to delete: ")
    if delete_item_from_list in buylist:
        buylist.remove(delete_item_from_list)
        print("Item has been Removed")
    else:
        print("Item isn't in the list")

def addItem(buylist):   #Add an item to the list
    add_item_to_list = input("Please enter the Item you want to add to the list: ")
    buylist.append(add_item_to_list)
    print(add_item_to_list, "Has been added to the list.")

def printIllegal(buylist):      #Prints illegal items (Non English or shorted than 3 letters)
    illegal = []
    for i in buylist:
        if len(i) < 3 or i.isalpha() == False:
            illegal.append(i)
            continue
    if len(illegal) > 1:
        print("The illegeal Items on the list are:", ", ".join(illegal))
    else:
        print("There are no illegal items on the list")

def deleteDuplicates(buylist):      #Deletes duplicate items from the list
    for i in buylist:
        while buylist.count(i) >= 2:
            buylist.remove(i)
    print("Duplicates has been removed")




def shoppinglist():
    buylist = input("Please enter Items to buy: ")
    buylist = buylist.split(",")    #Splits the list for indivitual item
    
    while True: 
        user_input = int(input("Please Enter a number from 1 to 9: "))
        if user_input == 1:    #Prints the list's content
            printList(buylist)
            continue
        elif user_input == 2:   #Prints the amount of items in the list
            printListAmount(buylist)
            continue
        elif user_input == 3:   #Checks if the item is on the list
                checkItem(buylist)
                continue
        elif user_input == 4:   #Prints the quantity of an item the users chooses
            printQuantity(buylist)
            continue
        elif user_input == 5:   #Deletes an Item from the list
            deleteItem(buylist)
            continue
        elif user_input == 6:   #Adds an Item to the list
            addItem(buylist)
            continue
        elif user_input == 7:   #Prints out the Illegal items (Items that aren't English Characters and they are less than 3 letters)
            printIllegal(buylist)
            continue
        elif user_input == 8:   #Deletes duplicates from the list
            deleteDuplicates(buylist)
            continue
        elif user_input == 9:   #Exiting the program
            print("You've Exited the program, Good Bye!")
            break



def main():
    shoppinglist()

if __name__ == '__main__':
    main()