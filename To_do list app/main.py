import time

to_do_list = []

print("Welcome to the to do list.")
time.sleep(3)
print("You can:")
time.sleep(0.5)
print("1. view the to do list.")
time.sleep(3)
print("2. add something to the to do list")
time.sleep(3)
print("3. take something away from the list")
time.sleep(3)
print("4. Exit")
time.sleep(3)

while True:
    ans = input("Which one of these options do you want to do? ")

    if ans == "1":
        if len(to_do_list) == 0:
            print("There is nothing in the list for you to view please try adding something first before viewing the list!")
        else:
            for i in to_do_list:
                print(f"the items in your list are\n{i}")

    elif ans == "2":
        added_attribute = input("What do you want to add to the to do list?")
        to_do_list.append(added_attribute)
        print(f"you have added {added_attribute} to the to do list!\n" )

    elif ans == "3":
        attribute_to_take_away = input("What do you want to take away from this list?")
        if attribute_to_take_away in to_do_list:
            to_do_list.remove(attribute_to_take_away)
            print(f"{attribute_to_take_away} is removed from the list\n")
        else:
            print("This attribute is not in the list\n")

    elif ans == "4":
     print("Hope to see you again!")
     break
        