from cars.actions import add_car, list_cars, delete_car, search_car, exit
from problems.problem_menu import select_problems

def menu_selection(cars, choice):
    if choice == "1":
        list_cars(cars)
    elif choice == "2":
        add_car(cars)
        selected_problems, total_price = select_problems()  
        print(f"The Price Of Your Fix Is: {total_price} NIS.")
        proceed = input("Do you wish to proceed? (Yes/Nope): ").lower()
        if proceed == "yes":
            pass
        else:
            print("Cancelled.")
    elif choice == "3":
        delete_car(cars)
    elif choice == "4":
        search_car(cars)
    elif choice == "5":
        exit(cars)
