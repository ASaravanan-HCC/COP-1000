# CarFinder Program for AutoCountry
def main():
    allowed_vehicles_list = [
        'Ford F-150',
        'Chevrolet Silverado',
        'Tesla CyberTruck',
        'Toyota Tundra',
        'Nissan Titan',
        'Rivian R1T',
        'Ram 1500'
    ]

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
            print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in allowed_vehicles_list:
                print(vehicle)
            print("********************************")
        elif user_input == "2":
            search_vehicle = input("Please Enter the full Vehicle name: ")
            if search_vehicle in allowed_vehicles_list:
                print(f"{search_vehicle} is an authorized vehicle")
            else:
                print(f"{search_vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")
            print("********************************")
        elif user_input == "3":
            new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
            allowed_vehicles_list.append(new_vehicle)
            print(f'You have added "{new_vehicle}" as an authorized vehicle')
            print("********************************")
        elif user_input == "4":
            delete_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
            if delete_vehicle in allowed_vehicles_list:
                confirm = input(f'Are you sure you want to remove "{delete_vehicle}" from the Authorized Vehicles List? (yes/no): ')
                if confirm.lower() == 'yes':
                    allowed_vehicles_list.remove(delete_vehicle)
                    print(f'You have REMOVED "{delete_vehicle}" as an authorized vehicle')
                else:
                    print(f'"{delete_vehicle}" was not removed from the Authorized Vehicles List')
            else:
                print(f"{delete_vehicle} is not in the Authorized Vehicles List")
            print("********************************")
        elif user_input == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
