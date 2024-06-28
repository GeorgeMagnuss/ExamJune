from cars.menu import menu_selection
from problems.problem_menu import select_problems
from problems.problems import problems_list

cars = [{"car": "Kia", "car_number": 2000}, {"car": "BMW", "car_number": 2001}]

def total_num_cars(cars):
    return len(cars)

def total_profit(cars):
    total_profit_value = sum(problems_list[problem] for problem in problems_list)
    return total_profit_value

def show_cars_and_profit(cars):
    num_cars = total_num_cars(cars)
    total_profit_value = total_profit(cars)
    print(f"Currently there are {num_cars} cars. The current profit is: {total_profit_value} NIS.")

def menu(cars):
    show_cars_and_profit(cars)  
    while True:
        print("\nWelcome to the Garage")
        print("1 - List All cars")
        print("2 - Add a Car")
        print("3 - Delete Car")
        print("4 - Search Car")
        print("5 - Exit")
        choice = input("Enter your choice: ")
        menu_selection(cars, choice)

if __name__ == "__main__":
    menu(cars)
