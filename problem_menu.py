from problems.problems import problems_list

def display_all_problems(problems):
    print("Garage Problems Menu:")
    index = 1
    for problem_name, problem_price in problems.items():
        print(f"{index}. {problem_name} - Price: {problem_price} NIS")
        index += 1

def select_problems():
    selected_problems = []
    while True:
        display_all_problems(problems_list)
        choice = input("Enter problem number to select (7 to finish): ")
        if choice == "7":
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(problems_list):
                selected_problem = list(problems_list.keys())[index]
                selected_problems.append(selected_problem)
                print(f"{selected_problem} added to list.")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    total_price = sum(problems_list[problem] for problem in selected_problems)
    print(f"Total Price for selected problems: {total_price} NIS")
    return selected_problems, total_price
