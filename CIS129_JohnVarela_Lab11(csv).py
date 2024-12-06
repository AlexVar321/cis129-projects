import csv
'''
    script: CIS129_JohnVarela_lab11(csv).py
    action: a. gets students name from user
            b. gets grades for 3 exams
            c. stores data in csv file
    author: John Alex Varela
    date:   12/05/2024
'''



def main():
    '''
    Main method to open csv file and get input from user make sure names are
    using alphabetical values then checks for grades for 3 exams that are
    within 0-100% otherwise it will ask you to repeat the process.

    action: gets valid student name from user
            gets valid grade for exams from user
            stores valid values
    input:  alphabetical string from user for student name
            float from user within 0-100% for the students exam grade
    output: student first and last name
            grade for each exam
            all in csv file
    return: student first and last name
            grade for each exam
            all in csv file
    '''

    # Opens a csv file in append mode
    with open("grades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        
        print("Enter student data (first and last name, and three exam grades)"
              ". Type 'done' to finish.")
        
        # Loop for getting student names and grades until no more names
        # are necessary
        while True:
            # Getting names or sentinal value "done" 
            first_name = input("Enter first name (or 'done' to finish): "
                               ).strip()
            if first_name.lower() == "done":
                print("Student data has been saved to grades.csv.")
                break
            # Validate first name
            if not is_valid_name(first_name):
                print("Invalid first name. Please use alphabetical"
                      " characters only.")
                continue
            
            last_name = input("Enter last name: ").strip()

            # Validate last name
            if not is_valid_name(last_name):
                print("Invalid last name. Please use alphabetical"
                      " characters only.")
                continue

            # gets grades from user and checks if the input was a float and
            # will store 3 values
            try:
                grades = [
                    round(float(input(f"Enter grade for Exam {i+1}: ").strip())
                          , 2) for i in range(3)
                ]
            except ValueError:
                print("Invalid grade. Please enter numeric grades only.")
                continue
            
            # Ensure all grades are between 0 and 100
            if all(0 <= grade <= 100 for grade in grades):

                # Write the record to the csv file
                writer.writerow([first_name, last_name, *grades])
                print(f"Record for {first_name} {last_name} added.")
            else:
                print("All grades must be between 0 and 100. Please try again.")

def is_valid_name(name):
    '''
    Function to check if my string is made of alphabetical values

    action: tests to see if string only has alphabetical values
    input: none
    output: none
    return: string consisting of alphabetical values
    '''
    return name.isalpha()
main()