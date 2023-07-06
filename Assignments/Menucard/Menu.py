#menu options
#1)Add
#2)Delete
#3)display
#4)edit

Menu_list=["Paneer Tikka","Masala Dosa","Aloo Paratha","Ice-Cream"]
print("Menu Card\n")
print("1) Add Items")
print("2) Delete Items")
print("3) Display Menu")
print("4) Edit Menucard")
print("5) Exit\n")

choice=input("\nEnter Your Choice: ")

if choice=="1":
    print(Menu_list)
    item=input("Enter the Item Name: ")
    Menu_list.append(item)
    print(f"{item} added sucessfully")
    print(Menu_list)

elif choice=="2":
        print(Menu_list)
        item1=input("Enter then item yoy want to delete: ")
        if item1 in Menu_list:
            Menu_list.remove(item1)
            print(f"{item1} removed sucessfully")
        else:
            print(f"{item1} not found in the menu.")
        print(Menu_list)
        
elif choice == "3":
    print("Menu Card\n",Menu_list[:])

elif choice == "4":
    print(Menu_list)
    edit=input("Enter the Item you want to edit: ") 
    if edit in Menu_list:
        new_item=input("Enter the new item: ")
        index=Menu_list.index(edit)
        Menu_list[index]=new_item
        print(f"{edit} updated to {new_item} successfully.")
        print(Menu_list)
    else:
        print(f"{edit} not found in the menu.")
         
elif choice == "5":
    print("Goodbye!")
else:
    print("Invalid choice. Please try again.")








