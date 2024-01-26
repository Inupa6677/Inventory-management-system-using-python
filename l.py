from tabulate import tabulate
import random
import datetime

def greet_user():
    print("Welcome to the one net cafe")
    return


greet_user()
dealers_that_selected = ""
dealer_list = []
item_list = []
dealer_items = []
name_list = []
adding_items = {}
any_duplicate_values = []


def add_items():
    global item_code, item_price, item_quantity
    #asume that item code consists only with integers
    while True:
        try:
            item_code = int(input("Enter the item code:"))
            if item_code < 0:
                print("please enter a valid code grater than 0 ")
                continue
            if item_code in any_duplicate_values:
                print("\n You have already added this item code ")
                continue
            else:
                any_duplicate_values.append(item_code)
            break
        except ValueError:
            print("Invalid input. You can try again ")
    while True:
        #assume that item name has only english letters
        try:
            item_name = input("Enter the name of the item:")
            if not item_name.isalpha():
                print("Invalid name please enter the the correct item name")
                continue
            break
        except ValueError:
            print("Invalid name. Please enter the the correct item name")
    while True:
        # assume that item name has only english letters
        try:
            item_brand = input("Enter the brand of the item:")
            if not item_brand.isalpha():
                print("Invalid brand. Please enter the correct item brand")
                continue
            break
        except ValueError:
            print("Invalid brand. Please enter the correct item brand")



    while True:
        # assume that item name has floating value
        try:
            item_price = float(input("Enter the price of the item: "))
            if item_price <= 0:
                print("Invalid price and please enter a valid price")
                continue
            break
        except ValueError:
            print("Invalid price and please enter a valid price")


    while True:
        # assume that item name has only integers
        try:
            item_quantity = int(input("Enter the amount of items:"))
            if item_quantity <= 0:
                print("Invalid quantity. Please enter the valid amount")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a valid quantity")
    while True:
        # assume that item name has only english letters
        try:
            item_category = input("Enter the item category:")
            if not  item_category.isalpha():
                print("Invalid category. please enter the correct category")
                continue
            break
        except ValueError:
            print("Invalid category. please enter the correct category")
    while True:
        try:
            purchased_date = input("Enter the purchasing date (yyyy-mm-dd):")
            purchased_date = datetime.datetime.strptime(purchased_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please enter a valid date ")


    adding_items[item_code] = {"Item code": item_code,
                               "Item name": item_name,
                               "Item brand": item_brand,
                               "Item price": item_price,
                               "Item quantity": item_quantity,
                               "Item category": item_category,
                               "Purchased date": purchased_date,
                               }
    while True:
        input1 = input('You want to add another item (yes/no): ')
        try:
            if input1.lower() == "yes":
                add_items()
            elif input1.lower() == "no":
                main_menu()
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input")


def delete_items():
    try:
        item_to_delete = int(input("Enter the item code of the item that you need to delete:"))
        if item_to_delete in adding_items:
            del adding_items[item_to_delete]
            print("Item deleted sucsessfully")

        elif item_to_delete not in adding_items:
            print("Item code not found")
    except ValueError:
        print("Invalid Input.Please Try Again.")

    while True:
        input_2 = input("Do you want to delete another item?")
        try:
            if input_2.lower() == "yes":
                delete_items()
            elif input_2.lower() == "no":
                main_menu()
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Try Again")


def update_items():
    global item_to_update, update_name
    while True:
        try:
            item_to_update = int(input("Enter the item code of the item that you need to update:"))
            if item_to_update <= 0:
                print("Invalid input. please enter a valid item code")
                continue
            break
        except ValueError:
            print("Invalid input. please enter a valid item code")
    while True:
        if item_to_update in adding_items:
            while True:
                try:
                    update_name = input("If you wants to update item name? please enter (yes/no): ")

                    if update_name == "yes":
                        new_name = input("Enter the new name: ")
                        adding_items[item_to_update]["Item_name"] = new_name
                        print("Name updated successfully.")
                    elif update_name.lower() == "no":
                        pass
                    elif not update_name.isalpha() or update_name != "yes" or update_name != "no":
                        print("Invalid input. Please check again ")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please check again")
            while True:
                try:
                    update_brand = input("Do you wants to update the item brand? please enter (yes/no): ")

                    if update_brand == "yes":
                        new_brand = input("Enter the new brand name: ")
                        adding_items[item_to_update]["Item_brand"] = new_brand
                        print("Item brand updated successfully.")
                    elif update_brand.lower() == "no":
                        pass

                    elif not update_brand.isalpha() or update_brand != "yes" or update_brand != "no":
                        print("Invalid input. Please check again ")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please check again")

            while True:
                try:
                    update_price = input("If you wants to update item price? please enter (yes/no): ")

                    if update_price == "yes":
                        new_price = float(input("Enter the new price: "))
                        adding_items[item_to_update]["Item_price"] = new_price
                        print("Item price updated successfully.")
                    elif update_price.lower() == "no":
                        pass
                    elif not update_price.isdigit() or update_price != "yes" or update_price != "no":
                        print("Invalid input. Please check again ")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please check again")

            while True:
                try:
                    update_quantity = (input("Do you wants to update the item quantity? please enter (yes/no): "))

                    if update_quantity == "yes":
                        new_quantity = int(input("Enter the new quantity: "))
                        adding_items[item_to_update]["Item quantity"] = new_quantity
                        print("Item quantity updated successfully.")
                    elif update_quantity.lower() == "no":
                        pass
                    elif not update_quantity.isdigit() or update_quantity != "yes" or update_quantity != "no":
                        print("Invalid input. Please check again")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please check again")

            while True:
                try:
                    update_category = input("Do you wants to update item category? please enter (yes/no): ")

                    if update_category == "yes":
                        new_category = input("Enter the new category: ")
                        adding_items[item_to_update]["Item category"] = new_category
                        print("Item category updated successfully.")
                    elif update_category.lower() == "no":
                        pass


                    elif not update_brand.isalpha() or update_brand != "yes" or update_brand != "no":
                        print("Invalid input. Please check again")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please check again")

            while True:
                try:
                    update_purchased_date = input("Do you wants to update item purchased date? please enter (yes/no)")

                    if update_purchased_date == "yes":
                        new_purchased_date = input("Enter the new purchased date (yyyy/mm/dd): ")
                        adding_items[item_to_update]["Purchased date"] = new_purchased_date
                        print("Item purchased date updated successfully.")
                    elif update_purchased_date.lower() == "no":
                        pass
                    elif update_purchased_date != datetime.datetime.strptime(update_purchased_date, "%Y-%m-%d") or update_purchased_date != "yes" or update_purchased_date != "no":
                        print("Invalid input. Please check again")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please check again")



        else:
            print("This item code was not found")
        main_menu()


def viewing_items():
    headers = ["Item code", "Item name", "Item brand", "Item price", "Item quantity", "Item category", "Purchased date"]
    rows = [[ item["Item code"], item["Item name"], item["Item brand"], item["Item price"], item["Item quantity"],
             item["Item category"], item["Purchased date"]] for item in adding_items.values()]

    n = len(rows)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if rows[j][0] < rows[j + 1][0]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]

    print(tabulate(rows, headers=headers))
    main_menu()

def saving_items():
    saving_to_file = open('inventory.txt', 'w')
    saving_to_file.write(str(adding_items))
    print("items saved sucsessfully")


def select_random_dealers():
    with open("dealers.txt", "r") as document:
        dealers = document.read().split("\n\n")
        global dealers_that_selected
        dealers_that_selected = random.sample(dealers, 4)
        print("Four dealers selected succsessfully ")
    main_menu()


def display_details_of_random_dealers():
    global dealers_that_selected
    print(dealers_that_selected)
    sort_dealers = dealers_that_selected
    lenth = len(sort_dealers)
    print(sort_dealers)
    print(lenth)
    for i in range(lenth-1):
        for j in range(0 , lenth-i-1):
            if sort_dealers [j][1] > sort_dealers [j+1][1]:
                sort_dealers[j], sort_dealers[j+1] = sort_dealers[j+1], sort_dealers[j]

    for dealer in sort_dealers:
        dealer_details = dealer.split("\n")
        dealer_name = dealer_details[0]
        contact_details = dealer_details[1]
        location = dealer_details[2]

        print(f" {dealer_name}")
        print(f" {contact_details}")
        print(f" {location}")

    print()
    main_menu()


def display_item_details():
    global dealer_items
    global dealers_that_selected
    for dealer in dealers_that_selected:
        a = dealer.split("\n")
        dealer_list.append(a)
    # print(dealer_list)

    for name in range(len(dealer_list)):
        raw_name = dealer_list[name][0]
        sliced_name = raw_name[11:]
        name_list.append(sliced_name)

    count = 0
    for name in name_list:
        dealer_list[count][0] = name
        count += 1


    count1 = 0
    name_input = input("Enter dealer's name:-")
    for item in dealer_list:
        if name_input == dealer_list[count1][0]:
            dealer_items = dealer_list[count1][3:6]
            count1 += 1

        else:
            count1 += 1
    for item in dealer_items:
        print(item)



def good_bye():
    print("Thank you good bye ")



def main_menu():
    print("Main menu")
    print("Type AID for adding item details")
    print("Type DID for deleting item details")
    print("Type UID for updating item details")
    print("Type VID for viewing the item table. (Sort according to the items category) and print the current total.")
    print("Type SID for saving the item details to the text file at any time ")
    print("Type SDD for selecting four dealers randomly from a file ")
    print("Type VRL for displaying all the details of the randomly selected dealers.(sorted according to the location.)")
    print("Type LDI for display the items of the given dealer.")
    print("Type ESC to exit the program.")
    user_choice = input("Enter Your choice from the main menu:-")
    print(user_choice)
    while True:
        try:
            if user_choice.upper() == "AID":
                add_items()
            elif user_choice.upper() == "DID":
                delete_items()
                main_menu()
            elif user_choice.upper() == "UID":
                update_items()
            elif user_choice.upper() == "VID":
                viewing_items()
            elif user_choice.upper() == "SID":
                saving_items()
                main_menu()
            elif user_choice.upper() == "SDD":
                select_random_dealers()
            elif user_choice.upper() == "VRL":
                display_details_of_random_dealers()
            elif user_choice.upper() == "LDI":
                display_item_details()
            elif user_choice.upper() == "ESC":
                good_bye()
            else:
                raise ValueError("Invalid option ")
            break
        except:
            print("Please input valid inputs only ")
            main_menu()


main_menu()
