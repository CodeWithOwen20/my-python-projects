# My Python Learning Journey

Welcome to my portfolio! This is my first central repository, where I document my independent computer science journey, storing the terminal applications and systems I build while teaching myself Python programming from scratch.



## Featured Projects

### 1. Monster Game V1
*A text-based RPG combat engine built to run natively within the terminal.*

* **Core Features:**
  * Secure player login validation system powered by custom Python dictionaries.
  * Dynamic, randomized monster encounters with automated enemy scaling.
  * Turn-based combat loop allowing players to strategically select battle actions.
  * Smart inventory healing system utilizing logical boundaries to prevent health overflowing past maximum limits.
    
* **Python Concepts Practised:**
  * Interactive infinite game loops (`while True`) and structured exit break sequences.
  * Nested conditional logic structures (`if / elif / else`).
  * Data collections (lists and dictionaries) to track real-time character states.
  * Practical integration of the standard library `random` module.



### 2. All-Type Multi-Calculator
*A multi-tool calculator that brings arithmetic operations and unit conversion directly to your command line.*

* **Core Features:**
  * **Core Mathematics:** Quick-access calculation suite supporting addition, subtraction, multiplication, and division.
  * **Distance Converter:** Instant mileage conversion from Miles to Kilometers.
  * **Temperature Converter:** Seamless conversion from Celsius to Fahrenheit.
    
* **Python Concepts Practised:**
  * **Input Type-Casting:** Deepening comprehension of data boundaries by strictly converting string-based terminal inputs into computational `float` objects.
  * **Functional Isolation:** Wrapping calculations into separate reusable functional blocks for cleaner code maintenance.
  * **Persistent UI Control Loops:** Keeping the application engine alive indefinitely so users can make sequential mistakes without crashing the runtime.



### 3. Personal Budget & Expense Engine
*A financial tracking application incorporating data persistence, CRUD logic, and defensive software hardening.*

* **Core Features:**
  * **30/50/10 Budget Splitter:** Automatically splits baseline wages into precise needs, wants, and savings accounts, cleanly formatted as currency (`:.2f`).
  * **Persistent Local Databases:** Implements permanent file tracking to allow users to write, append, review, or wipe historical data records over multiple sessions.
  * **Volatile "Ghost File" Popups:** Hooks directly into native Windows directories (`os` and `tempfile`) to launch a temporary welcome documentation window upon script start up.
    
* **Python Concepts Practised:**
  * **File I/O & Context Managers:** Safe data stream manipulation using the standard `with open()` paradigm alongside specific file permissions (`"r"`, `"w"`, `"a"`).
  * **Defensive Exception Handling:** Hardening software against failure states by trapping runtime errors (like `FileNotFoundError`) using `try / except` isolation traps.
  * **Data Normalization:** Using string methods like `.strip()` and `.lower()` to eliminate capitalization conflicts and hidden file whitespace errors.



## How To Run These Projects

### Prerequisites
Ensure you have **Python 3** installed on your pc/laptop. You can verify this by opening your command prompt and running `python --version`.

### Step-by-Step Execution
1. Clone this repository or download the specific `.py` script you want to test.
2. Open your terminal or Command Prompt (`cmd`).
3. Navigate to the local folder directory where the script is saved.
4. Execute the file by typing the corresponding command below:

```bash
# Launch the RPG Combat Game
python textgame.py

# Launch the Multi-Calculator Utility
python all_type_calculator.py

# Launch the Budget Tracking Engine
python budget_tracker.py
