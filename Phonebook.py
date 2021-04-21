'''
-> datastructure
     - Fullname
     - Phonenumber
     - Email
-> Add a new item to phone book
-> List items from book
-> Remove item from book
-> Search items from book
-> Store book data to a file
-> Reload data when we start

Notes:
cmd prompt for windows
terminal for linus/mac
$ pip install requests
'''

import csv
filename = "phonebook_python.csv"
print("\n-------------------Welcome to the Phonebook------------------\n")



def add_item(phonebook, *, name, number, email):
    bookitem = {"fullname": "", "number": "", "email": ""}
    bookitem["fullname"] = name
    bookitem["number"] = number
    bookitem['email'] = email
    phonebook.append(bookitem)


def search_item(phonebook, keyword):
    for index, item in enumerate(phonebook):
        if keyword.lower() in item["fullname"].lower():
            print("\nFound => Name: {} | PhoneNumber: {} | Email: {} | Index: {}\n".format(
                item["fullname"], item["number"], item["email"], index
                ))
    print("-"*60)



def update_item(phonebook, keyword):
    items =[]
    for index, item in enumerate(phonebook):
        if keyword.lower() in item["fullname"].lower():
            print("\nFound => Name: {} | PhoneNumber: {} | Email: {} | Index: {}\n".format(
                item["fullname"], item["number"], item["email"], index
                ))
            index_item = phonebook[index]
            phonebook.pop(index)
            while True:
                name = input('Enter updated full name: ')
                if not name.strip():
                    print("\nFullname cannot be empty. Please continue")
                    continue
                number = input('Enter updated Phone Number: ')
                if not number.strip():
                    print("\nPhonenumber cannot be empty. Please continue")
                    continue
                email = input('Enter updated Email: ')
                if not email.strip():
                    print("\nEmail cannot be empty. Please continue")
                    continue
                index_item.update({"fullname":name, "number":number, "email":email})
                phonebook.insert(index, index_item)
                break
            print("\nUpdated record => Name: {} | PhoneNumber: {} | Email: {} | Index: {}\n".format(
                name, number, email, index                
                ))
    print("-"*60)
    


def remove_item(phonebook, keyword):
    for index, item in enumerate(phonebook):
        if keyword.lower() in item["fullname"].lower():
            print("\nFound => Name: {} | PhoneNumber: {} | Email: {} | Index: {}\n".format(
                item["fullname"], item["number"], item["email"], index
                ))
            sure = input("\nAre you sure, you want to remove this item permanently? [y/yes]: ")
            if not (sure.lower() == "y" or sure.lower() == "yes"):
                 break
            else:
                phonebook.pop(index)
                print("\nThis record has been successfully deleted.")
            
    print("-"*60)   
            
             
def list_items(phonebook):
    print("-"*60)
    print("FullName\t|\tPhoneNumber\t|\tEmail", end="\n")
    print("-"*60)
    for item in phonebook:
        print("{}\t\t{}\t\t{}".format(
            item["fullname"],item["number"],item["email"]
        ))
    print("-"*60)


def add_action():
    items = []
    while True:
         fullname = input('Enter full name: ')
         if not fullname.strip():
             print("\nFullname cannot be empty. Please continue")
             continue   
         ph_number = input('Enter Phone Number: ')
         if not ph_number.strip():
             print("\nPhonenumber cannot be empty. Please continue")
             continue
         num_check = is_duplicate_number(phonebook, ph_number)
         if num_check is True:
             continue
         email = input('Enter Email: ')
         if not email.strip():
             print("\nEmail cannot be empty. Please continue")
             continue
         email_check = is_duplicate_email(phonebook, email)
         if  email_check is True:
            continue
         items.append((fullname, ph_number,email))
         char = input("\nDo you want to continue? [y/yes]: ")
         if not (char.lower() == "y" or char.lower() == "yes"):
                break
    return items


def is_duplicate_number(phonebook, ph_number):
    for index, item in enumerate(phonebook):
        if ph_number in item["number"]:
            print("This phone number already exists.")
            return True        
            
            

def is_duplicate_email(phonebook, email):
    for index, item in enumerate(phonebook):
        if email in item["email"]:
            print("This email already exists.")
            return True    
            #this function should return True if email is already present in phonebook and return False if email is not present

            
            
        
#default argument
def write_to_csv(phonebook, filename, write_mode = "w"):
        with open(filename, write_mode) as csvfile:
               writer = csv.DictWriter(csvfile, fieldnames=["fullname","number", "email"])
               writer.writeheader()
               for each in phonebook:
                   writer.writerow(each)
                   

def cli():
    global phonebook
    global filename
    phonebook = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['fullname','number','email'])
        next(reader)
        phonebook.extend(reader)
    while True:
        print("""
        Select your Action:
        
        A: Add
        L: List
        S: Search
        U: Update
        R: Remove
        E: Exit
        """)
        action = input("Please select an action: ")
        if action.upper() == "A":
             collected_items = add_action()
             for name, number, email in collected_items:
                 add_item(phonebook, name=name, email=email, number=number)
        elif action.upper() == "L":
             list_items(phonebook)
        elif action.upper() == "S":
             keyword = input("\nEnter a keyword to search: ")
             search_item(phonebook,keyword)
        elif action.upper() == "U":
             keyword = input("\nEnter the name whose record is to update: ")
             update_item(phonebook, keyword)
        elif action.upper() == "R":
            keyword = input("\nEnter the name whose record is to remove: ")
            remove_item(phonebook,keyword)
        elif action.upper() == "E":
            write_to_csv(phonebook, filename)
            break
        else:
             print("\nInvalid Action Selected")
             

print(__name__)
if __name__ == "__main__":
    cli()
    
             
