'''
    script: CIS129_JohnVarela_lab12.py
    action: a. gets details about a pet from user
            b. stores data in class called pet
            c. displays pets details
    author: John Alex Varela
    date:   12/12/2024
'''

class Pet:
    def __init__(self, name="", type="", age=0):
        '''
        Initializes pet object with optional values for the name of the pet,
        the type of pet, and the age of the pet

        action: Initializes object and stores data
        input: name type and age from user
        output: none
        return: none
        '''
        self.name = name
        self.pet_type = type
        self.age = age
    def setName(self, name):
        '''
        stores name of the pet from user

        action: gets name of pet
        input: name from user
        output: none
        return: none
        '''
        self.name = name
    def setType(self, type):
        '''
        stores type of animal pet is

        action: stores type of animal pet is
        input: pet type from user
        output: none
        return: none
        '''
        self.type = type
    def setAge(self, age):
        '''
        stores the age of pet

        action: stores the age of pet
        input: age of pet from user
        output: none
        return: none
        '''
        self.age = age
    def getName(self):
        '''
        returns value of the pets name input from the user 

        action: returns value of the pets name input from the user
        input: name of users pet
        output: name of users pet
        return: name of users pet
        '''
        return self.name
    def getType(self):
        '''
        returns animal type pet is, input from user

        action: returns animal type pet is, input from user
        input: animal type
        output: animal type 
        return: animal type
        '''
        return self.type
    def getAge(self):
        '''
        returns pets age integer input by user

        action: returns pets age integer input by user
        input: pets age integer
        output: pets age integer
        return: pets age integer
        '''
        return self.age
    

def main():
    '''
	main method to get input from user and print results from the class

	action: gets input from user then prints result
	input: pets name
           pets animal type
           pets age
	output: pets name
            pets animal type
            pets age
	return: pets name
            pets animal type
            pets age
	'''
    # variable to access object
    my_pet = Pet()

    # variables to collect data from user
    name = getString("Enter the name of your pet:\n")
    pet_type = getString(f"Enter what type of pet {name} is (dog, cat, bird, etc.):\n")
    pet_age = getInt(f"Enter how old {name} is:\n")

    # sends data to class
    my_pet.setName(name)
    my_pet.setType(pet_type)
    my_pet.setAge(pet_age)
    
    # prints result from class
    print("\nYour pet's details:")
    print(f"Name: {my_pet.getName()}\nType: {my_pet.getType()}\n"
          f"Age: {my_pet.getAge()} years")


def getString(prompt):
    '''
	gets a string that excludes special characters

	action: gets a string that excludes special characters
            sends error if string includes non alphabetic characters
	input: string from user
	output: string
	return: string
	'''

    # while loop to get valid input
    while True: 
        name = input(prompt)

        # makes the first letter uppercase and sends string back
        if name.isalpha():
           finalName = name[:1].upper() + name[1:]
           return str(finalName)
        else:
            print("Please don't use special characters\n")

def getInt(prompt):
    '''
	gets an integer from user

	action: gets an integer from user
            sends error if input is not an integer
	input: integer from user
	output: integer
	return: integer
	'''   

    # while loop to get valid input
    while True:
        integer = (input(prompt))
        if integer.isdigit() > 0:
            return int(integer)
        else:
            print("Please enter your pet's age in years\n")


        

if __name__ == "__main__":
    main()
    
        
            