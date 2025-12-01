import core_functionality as cf_

def create(main_dict, group_dict, fieldnames):
    print("Welcome to Create mode")
    print("Create a new ")
    return main_dict, group_dict

def read(main_dict, group_dict, fieldnames):
    return main_dict, group_dict

def update(main_dict, group_dict, fieldnames):
    return main_dict, group_dict

def delete(main_dict, group_dict, fieldnames):
    return main_dict, group_dict

# simply display the menus of what to do
def display_menu():
    print('''
SELECT THE NUMBER FOR THESE ACTIONS :
>>> 1. CREATE
>>> 2. READ__
>>> 3. UPDATE
>>> 4. DELETE
>>> 5. Exit__''')
    return