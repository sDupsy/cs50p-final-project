#  Dog Calorie Calculator and Tracker

### Video Demo:
[Watch on YouTube](https://www.youtube.com/watch?v=tTaL5PB3hrU)

---

###  Description:
This is a Calorie Calculator and Tracker for Dogs — well, more precisely, it's a tool for humans who want to monitor their dog’s daily caloric needs based on weight and activity level. Users can add, update, list, or delete dog entries, and the app stores everything in a `dogs.csv` file.

---

##  How It Works

### Global List: `dogs`
A global list is used to store all dog data in memory during runtime. This ensures all edits are made before writing everything back to the CSV file at once, reducing I/O operations and keeping things efficient.

---

##  Functions Overview

### `main()`
- Checks if `dogs.csv` exists.
  - If not, creates it with headers.
  - If it exists, loads dogs from it.
- Depending on whether dogs are listed, either:
  - Calls `list_dogs()` and then `check_action()`  
  - Or directly calls `make_new()`

---

### `get_name()`
- Prompts the user to enter a dog's name.
- Ensures the input only contains letters.
- Capitalizes and returns the name.

---

### `get_weight(name)`
- Asks for the dog's weight in kilograms.
- Validates the input and returns it as a float.
- Includes the name in prompts for readability.

---

### `get_activity(name)`
- Asks how active the dog is: `Very`, `Normal`, or `Lightly`.
- Validates input against a list of accepted levels.
- Returns the chosen level as a lowercase string.

---

### `calc_kcal(weight, activity)`
- Uses the formula:  
kcal = (weight ** 0.75) * activity_multiplier

 - Multiplier based on activity level:
- `Very` → 130
- `Normal` → 119
- `Lightly` → 108
- Returns the result as a rounded integer.

---

### `check_action()`
- Main loop asking the user what to do next:
- `N`: Add a new dog (`make_new()`)
- `L`: List all dogs (`list_dogs()`)
- `C`: Change dog stats (`change_dog()`)
- `D`: Delete dogs (`delete()`)
- `E`: Save and exit (`exit()`)

---

### `make_new()`
- Collects name, weight, and activity.
- Calculates calories.
- Appends a new dog entry to the list.
- Confirms the entry and loops back with `check_action()`.

---

### `list_dogs()`
- Iterates over all dogs in the list.
- Displays name, weight, activity level, and recommended kcal.
- Then calls `check_action()` again.

---

### `change_dog()`
- Prompts for the name of the dog to modify.
- Lets user change:
- Name
- Weight (updates kcal)
- Activity level (updates kcal)
- Validates input and updates the list.
- Calls `check_action()` afterward.

---

### `delete()`
- Asks if the user wants to delete:
- All dogs → clears the list
- A specific dog → removes that dog by name
- Then loops back with `check_action()`

---

### `exit()`
- Writes all current dog entries into `dogs.csv`.
- Saves data permanently.
- Exits the program with a goodbye message.

---

## File Overview

- `project.py`: Main application code
- `dogs.csv`: Stores dog data (auto-created)
- `requirements.txt`: Dependency list (optional use)
- `test_project.py`: Placeholder for future tests

---

##  Final Words

I hope you enjoy my project.  
CS50P has been an incredible experience, and I truly appreciate everything the CS50 team has done for new coders like me. This project reflects my learning journey, and I'm proud of how far I've come.

---

 **Author**: Christopher Sanders  
🔗 GitHub: [@sDupsy](https://github.com/sDupsy)

