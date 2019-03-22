'''
    Shopping list management program
    H223 76 Software Design and Development
    Aurélien Ammeloot
    Started 22 March 2019
'''

def display_options():
    print(""" Welcome to the shopping list program
    -----------------------------------------
    1. Add an item
    2. Remove an item
    3. Show all items
    4. Save to file
    5. Load from file
    6. Quit
    -----------------------------------------
    """)

# Set variable choice to zero
choice = 0

# First loop, managing the menu options
while choice != 6:
    display_options() # Display menu
    # Get user input
    choice = int(input("Please enter your selection: "))
    # input validation
    while choice < 1 or choice > 6:
        print("Error, invalid choice") # Error message
        display_options() # Menu (again)
        choice = int(input("Please enter your selection (1-6): "))
    
    # Handling the menu choices:
    if choice == 1:
        print("Choice 1")
    elif choice == 2:
        print("Choice 2")
    elif choice == 3:
        print("Choice 3")
    elif choice == 4:
        print("Choice 4")
    elif choice == 5:
        print("Choice 5")
    else:
        print("Bye!")
