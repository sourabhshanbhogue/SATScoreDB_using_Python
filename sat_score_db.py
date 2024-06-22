import json

sat_results = {}

#Checking if user has text only
def enter_valid_text(user_input):
    while True:
        if user_input.isalpha():
            break
        else:
            print("Please Enter using only Letters: ")
            user_input = input()
    return user_input
    
#Checking if user has entered a valid score
def enter_valid_score(num):
    while True:
        try:
            score = int(num)
            if 0 <= score <= 1600:
                break
            else:
                print("Please Enter a Score between 0 to 1600: ")
                num = input()
        except ValueError:
            print("Please Enter a Valid Number: ")
            num = input()
    return score

#Checking if user has passed or failed the SAT Exam
def check_exam_status(score):
    cutoff_percentage = 30.0
    max_sat_score = 1600
    sat_percentage = (score/max_sat_score)*100
    if (sat_percentage > cutoff_percentage):
        exam_status = "Pass"
    else:
        exam_status = "Fail"
    return exam_status

#User inserts name, address, city, country, pincode and SAT score.
def insert_data():
    while True:
        name = enter_valid_text(input("Enter Name: "))
        if name not in sat_results:
            break
        else:
            print(f"A Record with Name '{name}' already exists. Please Enter a different Name: ")

    address = input("Enter Address: ")
    city = enter_valid_text(input("Enter City: "))
    country = enter_valid_text(input("Enter Country: "))

    while True:
        pincode = input("Enter Pincode: ")
        if pincode.isdigit():
            break
        else:
            print("Please Enter using only Digits: ")

    sat_score = enter_valid_score(input("Enter SAT Score: "))
    exam_status = check_exam_status(sat_score)

    #Storing the user data
    sat_results[name] = {
        "Name": name,
        "Address": address,
        "City": city,
        "Country": country,
        "Pincode": pincode,
        "SAT Score": sat_score,
        "Exam Status": exam_status
    }
    print("Data Inserted Successfully.")
    
def view_all_data():
    print("Displaying All Records: ")
    print(json.dumps(sat_results, indent=2))
    
#Checking if record with name exists, if yes, display the SAT score associated with the name
def get_rank():
    name = enter_valid_text(input("Please Enter the Name to display their SAT Score: "))
    if name in sat_results:
        print(f"The SAT Score of {name} is: {sat_results[name]['SAT Score']}")
    else:
        print(f"No such records with '{name}' is found.")

#Checking if record with name exists, if yes, update the SAT score associated with the name
def update_score():
    name = enter_valid_text(input("Please Enter the Name to update their SAT Score: "))
    if name in sat_results:
        new_score = enter_valid_score(input("Enter new SAT Score:"))
        sat_results[name]["SAT Score"] = new_score
        sat_results[name]["Exam Status"] = check_exam_status(new_score)
        print("SAT Score Updated Successfully.")
    else:
        print(f"No such records with '{name}' is found.")

#Checking if record with name exists, if yes, delete that record
def delete_record():
    name = enter_valid_text(input("Please Enter the Name to delete their Record: "))
    if name in sat_results:
        del sat_results[name]
        print(f"Record with '{name}' is deleted successfully.")
    else:
        print(f"No such records with '{name}' is found.")

#saves the json to a file in the same location as the code
def save_to_file():
    with open("sat_results.json", "w") as file:
        json.dump(sat_results, file, indent=2)
    print("Data saved to sat_results.json")

#-----------Main Menu-----------
while True:
    print("\nMenu:")
    print("1. Insert data")
    print("2. View all data")
    print("3. Get rank")
    print("4. Update score")
    print("5. Delete one record")
    print("6. Save to file")
    print("7. Exit")

    choice = input("Enter your choice (1-7):")
    if choice == "1":
        insert_data()
    elif choice == "2":
        view_all_data()
    elif choice == "3":
        get_rank()
    elif choice == "4":
        update_score()
    elif choice == "5":
        delete_record()
    elif choice == "6":
        save_to_file()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")


