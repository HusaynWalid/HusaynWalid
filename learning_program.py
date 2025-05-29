import time

# Welcome Message
def welcome():
    print("\n🚀 Welcome to Your Interactive Python Learning Course!")
    print("This program will teach you Python step by step.")
    print("Type the correct answers to proceed.")
    print("Let's begin!\n")
    time.sleep(2)

# Lesson 1: Variables
def lesson_variables():
    print("\n📖 Lesson 1: Variables in Python")
    print("Variables store information. Example:")
    print("x = 5  # x now holds the value 5")
    print("y = 'Hello'  # y now holds the text 'Hello'")
    print("Variables can store numbers, text, and more!\n")
    
    answer = input("❓ What value is stored in x if we write: x = 10? ➡ ")
    if answer.strip() == "10":
        print("✅ Correct!")
    else:
        print("❌ Not quite! x stores whatever number you assign to it.")
    
    time.sleep(2)

# Lesson 2: Data Types
def lesson_data_types():
    print("\n📖 Lesson 2: Data Types")
    print("Different types of data exist in Python:")
    print("- int (Whole numbers) ➡ Example: 10")
    print("- float (Decimal numbers) ➡ Example: 3.14")
    print("- str (Text) ➡ Example: 'Hello world'")
    
    answer = input("❓ What type of data is: 'Python is fun'? (int, float, or str?) ➡ ")
    if answer.strip().lower() == "str":
        print("✅ Correct!")
    else:
        print("❌ Not quite! Strings (str) are text values.")
    
    time.sleep(2)

# Lesson 3: Loops
def lesson_loops():
    print("\n📖 Lesson 3: Loops")
    print("Loops help repeat code automatically.")
    print("Example:")
    print("for i in range(3):")
    print("    print('Python is awesome!')")
    print("This repeats 3 times!")
    
    answer = input("❓ What keyword starts a loop in Python? (for or if?) ➡ ")
    if answer.strip().lower() == "for":
        print("✅ Correct!")
    else:
        print("❌ Not quite! 'for' is used to create loops.")
    
    time.sleep(2)

# Lesson 4: Functions
def lesson_functions():
    print("\n📖 Lesson 4: Functions")
    print("Functions allow us to reuse blocks of code.")
    print("Example:")
    print("def greet(name):")
    print("    print('Hello ' + name + '!')")
    print("greet('Husayn')  # This prints: Hello Husayn!")
    
    answer = input("❓ What keyword defines a function in Python? ➡ ")
    if answer.strip().lower() == "def":
        print("✅ Correct!")
    else:
        print("❌ Not quite! 'def' is used to create functions.")
    
    time.sleep(2)

# Lesson 5: Debugging Tips
def lesson_debugging():
    print("\n🔍 Lesson 5: Debugging Tips")
    print("Debugging helps fix errors in code.")
    print("Common techniques:")
    print("- Print statements to check values")
    print("- Using Python's built-in debugger (`pdb`)")
    print("- Reading error messages carefully")

# Lesson 6: Algorithms
def lesson_algorithms():
    print("\n⚡ Lesson 6: Introduction to Algorithms")
    print("Algorithms are step-by-step instructions for solving problems.")
    print("Example:")
    print("Sorting numbers in ascending order.")
    print("Common algorithms:")
    print("- Searching (Binary Search)")
    print("- Sorting (Bubble Sort, Quick Sort)")
    
    answer = input("❓ What type of algorithm finds items quickly in sorted lists? ➡ ")
    if answer.strip().lower() == "binary search":
        print("✅ Correct!")
    else:
        print("❌ Not quite! Binary Search helps find items fast.")

# Final Exam Section
def final_exam():
    print("\n🎯 Final Exam Section!")
    print("Now, write a Python program that does the following:")
    print("1. Creates a variable called 'score' and sets it to 100.")
    print("2. Defines a function that prints: 'Your score is ' + score.")
    print("Try coding this yourself in Python and run it!")

# Progress Tracking System
def track_progress():
    print("\n🏆 Tracking Your Progress")
    print("You've completed lessons on variables, loops, functions, debugging, and algorithms!")
    print("Keep practicing to master Python.")

# Start the course
def start_course():
    welcome()
    lesson_variables()
    lesson_data_types()
    lesson_loops()
    lesson_functions()
    lesson_debugging()
    lesson_algorithms()
    final_exam()
    track_progress()
    print("\n🏆 Congratulations, Husayn! You've completed the Python basics course.")

# Run the program
start_course()