'''
    script: CIS129_JohnVarela_lab11.py
    action: a. gets grades
            b. stores data in txt file
            c. displays stored grades and the average of the grades
    author: John Alex Varela
    date:   12/05/2024
'''




def main():
    '''
    main function to open a txt file that stores grades and will average them out

    action: gets grade from user then stores grade and 
            will average all saved grades
    input: grade from user
    output: all grades and the average
    return: all grades and the average
    '''
    # Opens a txt file in append mode to add grades
    with open("grades.txt", "a") as file:
        print("Enter grades to store into grades.txt. Type 'done' to finish.")
        
        # While loop to get as many grades as wanted before entering sentinal
        while True:
            grade = input("Enter a grade: ").strip()
            if grade.lower() == "done":
                print("Grades have been saved to grades.txt.")
                break
            elif (grade.isdigit() or (grade.replace('.', '', 1).isdigit() and grade.count('.') == 1)) and float(grade) <= 100:
                file.write(grade + "\n")
                print(f"Grade {grade} added.")
            else:
                print("Invalid grade. Please enter a valid number or 'done'.")
    # Opens txt file in read mode to see the input grades and their average            
    try:
        
        with open("grades.txt", "r") as file:
            grades = file.readlines()
        
        # gets rid of white space and converts grades to a float then rounds
        grades = [round(float(grade.strip()), 2) for grade in grades if grade.strip().isdigit() or grade.strip().replace('.', '', 1).isdigit()]
        
        # prints all the grades
        if grades:
            
            print("Grades:")
            for grade in grades:
                print(f"- {grade}")
            
            # gets sum of all grades, how many grades were stored and average
            total = sum(grades)
            count = len(grades)
            average = total / count
            
            # prints the added grades how many grades input and the average
            print("\nStatistics:")
            print(f"Total: {total}")
            print(f"Count: {count}")
            print(f"Average: {average:.2f}")
        # error in case no valid values are found or no txt file found
        else:
            print("No valid grades found in the file.")
    except FileNotFoundError:
        print("The file 'grades.txt' does not exist. Please ensure it has been created.")
main()