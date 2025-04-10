import csv
import sys
import os

# all dogs allready listed
dogs = []


# imports csv to dogs and checks if dogs are listed. If not calls make_new else lists exsisting dogs and asks for action
def main() -> None:
    headers: list[str] = ["name", "weight", "activity", "kcal"]
    global dogs
    if not os.path.exists("dogs.csv"):
        with open("dogs.csv", mode="w") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            make_new()
    else:
        with open("dogs.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dogs.append(row)
            if dogs:
                list_dogs()
                check_action()
            else:
                make_new()


# checks dogs name for alphabetical and returns name as str
def get_name() -> str:
    while True:
        name: str = input("\nWhat is your dogs name? ").strip()
        if name.isalpha():
            return name.capitalize()
        else:
            print(
                "Im going to assume that your dogs Name only contains letters. Pls try again."
            )
            continue


# takes name for formating. checks and returns KG as float
def get_weight(name) -> float:
    while True:
        try:
            return float(input(f"How much does {name} weigh in KG? "))
        except ValueError:
            print("Pls pnly type the weight in KG (e.g: 10)")
            continue


# takes name for formating checks if valid activity and returns if so
def get_activity(name) -> str:
    levels: list[str] = ["very", "normal", "lightly"]
    while True:
        activity: str = input(f"How active is {name}? Very, normal or lightly? ").strip()
        if activity.lower() in levels:
            return activity
        else:
            print("Pls give me one of the above. ")


# takes weight in kg as float and activity level as string. converts activity to int and returns kcal
def calc_kcal(weight, activity) -> int:
    multiplier: dict[str, int] = {"very": 130, "normal": 119, "lightly": 108}
    return int(round((weight**0.75) * multiplier[activity]))


# checks input for valid action (new, list, change or exit) and calls corresponding function
def check_action() -> sys.NoReturn:
    global dogs
    while True:
        action: str = input(
            "\nTo add another dog type: 'N' \nTo see the stats of all listed dogs type: 'L'. \nTo change stats of a listed dog type: 'C'. \nTo delete one or all dogs type 'D'. \nTo exit type 'E'.\n"
        ).strip()
        if action.lower() == "n":
            make_new()
        elif action.lower() == "l":
            list_dogs()
        elif action.lower() == "c":
            change_dog()
        elif action.lower() == "d":
            delete()
        elif action.lower() == "e":
            exit()


# calls functions to get name (for formating), weight, activity, kcal and appends dict of dog to list of dogs, prints confirmation and asks for action
def make_new() -> None:
    global dogs
    name: str = get_name()
    weight: float = get_weight(name)
    activity: str = get_activity(name)
    kcal: int = calc_kcal(weight, activity)
    dogs.append({"name": name, "weight": weight, "activity": activity, "kcal": kcal})
    print(f"\n{name} has been added. The recomended calories per day are {kcal}. ")
    check_action()


# iterates through dogs and prints stats formated then asks for action
def list_dogs() -> None:
    global dogs
    for dog in dogs:
        print(
            f"\n{dog['name']} weighs {dog['weight']}KG is {dog['activity']} active and should eat {dog['kcal']} kcal per day."
        )
    check_action()


# takes name of dog to change, checks imput of what to change, calls functions if necessary, then iterates over dogs, changes as needed and asks for action
def change_dog() -> sys.NoReturn:
    global dogs
    while True:
        name: str = input("\nWhich dog would you like to change? ").strip().capitalize()
        if any(dog.get("name") == name for dog in dogs):
            while True:
                to_change: str = input(
                    f"\nWhat stat about {name} would you like to change?\nFor name type 'name', for the weight type 'weight',\nand for the activity level type 'activity'\n"
                )
                if to_change.lower() == "name":
                    new_name: str = get_name()
                    for dog in dogs:
                        if dog["name"] == name:
                            dog["name"] = new_name
                            print(f"\n{name}´s name has been changed to {new_name}.")
                            break
                    check_action()
                elif to_change.lower() == "weight":
                    try:
                        new_weight: float = get_weight(name)
                        for dog in dogs:
                            if dog["name"] == name:
                                dog["weight"] = new_weight
                                dog["kcal"] = round(calc_kcal(new_weight, dog["activity"]))
                                print(
                                    f"\n{name}´s weight has been changed to {new_weight} KG. His recommended calorie intake has been updated to {dog['kcal']}."
                                )
                                break
                        check_action()
                    except ValueError:
                        continue
                elif to_change.lower() == "activity":
                    try:
                        new_activity: str = get_activity(name)
                        for dog in dogs:
                            if dog["name"] == name:
                                dog["activity"] = new_activity
                                dog["kcal"] = calc_kcal(
                                    float(dog["weight"]), new_activity
                                )
                                print(
                                    f"\n{name}´s activity level has been changed to {new_activity}. His recommended calorie intake has been updated to {dog['kcal']}."
                                )
                                break
                        check_action()
                    except ValueError:
                        continue
        else:
            print(f"\nThe dog '{name}' is not in the list. Please try again.")
            continue



# asks if delete all or specific dog and does so
def delete() -> sys.NoReturn:
    global dogs
    while True:
        all_or_one = input("\nIf you want to delete all listed Dogs Type 'A' if you want to delete a specific Dog type the name.\n").strip().capitalize()
        if all_or_one.lower() == "a":
            dogs = []
            print("All Dogs have been deleted.\n")
            check_action()
        elif any(dog.get("name") == all_or_one for dog in dogs):
            dogs = [dog for dog in dogs if dog["name"] != all_or_one]
            print(f"{all_or_one} has been deleted.\n")
            check_action()
        else:
            continue


# writes final list of dogs to csv and exits
def exit() -> sys.NoReturn:
    global dogs
    field_names: list[str] = ["name", "weight", "activity", "kcal"]
    with open("dogs.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for dog in dogs:
            writer.writerow(dog)
    print("Until next time.")
    sys.exit()


if __name__ == "__main__":
    main()

