def list_cars(cars):
    for car in cars:
        print(car)

def add_car(cars):
    new_car = input("Enter car: ")
    new_car_number = input("Enter car number: ")

    new_car_data = {"car": new_car, "car_number": new_car_number}
    cars.append(new_car_data)
    print("New car Added: ", new_car_data)

def delete_car(cars):
    car_select = input("Choose car number: ")
    cars.pop(int(car_select))
    print("Car deleted")

def search_car(cars):
    def search():
        print("Search Initiated")
        search_str = input("Please enter search string: ")
        found = False
        for car in cars:
            if (
                search_str.lower() in car["car"].lower()
                or search_str.lower() in car["car_number"].lower()
            ):
                print(f"Car: {car['car']}, Car Number: {car['car_number']}")
                found = True

        if not found:
            print("Car Not Found!")

    search()

def exit(cars):
    print("Exiting Garage.")
