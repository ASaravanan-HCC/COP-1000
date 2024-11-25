import os

# File path for the Allowed Vehicles list
FILE_PATH = "allowed_vehicles.txt"

def load_vehicles():
    """Load vehicles from the file into a list."""
    if not os.path.exists(FILE_PATH):
        # Create the file with default vehicles if it doesn't exist
        with open(FILE_PATH, "w") as file:
            file.write("\n".join([
                'Ford F-150',
                'Chevrolet Silverado',
                'Tesla CyberTruck',
                'Toyota Tundra',
                'Rivian R1T',
                'Ram 1500'
            ]))
    with open(FILE_PATH, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_vehicles(vehicles):
    """Save the list of vehicles back to the file."""
    with open(FILE_PATH, "w") as file:
        file.write("\n".join(vehicles))

def print_all_vehicles(allowed_vehicles_list):
    """Display all authorized vehicles."""
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)
    print("********************************")

def search_vehicle(allowed_vehicles_list):
    """Search for a specific vehicle."""
    search_vehicle = input("Please Enter the full Vehicle name: ")
    if search_vehicle in allowed_vehicles_list:
        print(f"{search_vehicle} is an authorized vehicle")
    else:
        print(f"{search_vehicle} is not an authorized vehicle. Please check the spelling and try again.")
    print("********************************")

def add_vehicle(allowed_vehicles_list):
    """Add a new vehicle to the list."""
    new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
    if new_vehicle not in allowed_vehicles_list:
        allowed_vehicles_list.append(new_vehicle)
        save_vehicles(allowed_vehicles_list)
        print(f'You have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print(f'"{new_vehicle}" is already in the Authorized Vehicles List.')
    print("********************************")

def delete_vehicle(allowed_vehicles_list):
    """Delete a vehicle from the list."""
    delete_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if delete_vehicle in allowed_vehicles_list:
        confirm = input(f'Are you sure you want to remove "{delete_vehicle}" from the Authorized Vehicles List? (yes/no): ')
        if confirm.lower() == 'yes':
            allowed_vehicles_list.remove(delete_vehicle)
            save_vehicles(allowed_vehicles_list)
            print(f'You have REMOVED "{delete_vehicle}" as an authorized vehicle.')
        else:
            print(f'"{delete_vehicle}" was not removed from the Authorized Vehicles List.')
    else:
        print(f"{delete_vehicle} is not in the Authorized Vehicles List.")
    print("********************************")

def main():
    allowed_vehicles_list = load_vehicles()

    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")

    while True:
        print("Please Enter the following number below from the following menu:")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            print_all_vehicles(allowed_vehicles_list)
        elif user_input == "2":
            search_vehicle(allowed_vehicles_list)
        elif user_input == "3":
            add_vehicle(allowed_vehicles_list)
        elif user_input == "4":
            delete_vehicle(allowed_vehicles_list)
        elif user_input == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
