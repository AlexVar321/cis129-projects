'''
    script: CIS129_JohnVarela_lab8.py
    action: a. checks if element in string is a letter
            b. checks if word is a palindrome
            c. returns true if word is a palindrome and false if word isn't one
    author: John Alex Varela
    date:   10/24/2024
'''
def is_palindrome(word: str) -> bool:
    '''
    loops to check if the test case word is a palindrome

    action: uses a stack to append the letters in the first half of the word
            then pops each letter of the second half of the word to see if its
            equal to the appended letter
    input: none
    output: none
    return: true/false depending on if the word is a palindrome
    '''
    #check if element is a letter
    letter_count = 0
    for letter in word:
       if isalpha(letter):
          letter_count += 1

    #variable for my stack of letters   
    stack = []

    #variable for my incriment to run loop
    i=0

    #variable to count valid letters seen
    letters_seen = 0

    #while loop to check if word is a palindrome
    while i < len(word):
        letter = word[i]
        if isalpha(letter):

            #checks if we are at the middle element
            if letters_seen == letter_count//2 and letter_count%2 == 1:
                pass

            #checks if we are before the middle element and append the value
            elif letters_seen < letter_count//2:
                stack.append(letter)

            #checks if we are after the middle element and pops the value then
            #compares it to the last appended element to see if they are equal
            elif letters_seen >= letter_count//2:
                val = stack.pop()
                if val.lower() == letter.lower():
                    pass
                else:
                    return False
            letters_seen += 1
        i+=1
    return True

def isalpha(letter):
    '''
    makes sure that we only test the letters in the word

    action: checks if each element of the string is a letter and returns true
            or false depending on if the element is a letter
    input: none
    output: none
    return: true/false depending if the element is a letter
    '''

    #set of checks using ASCII to check for letters capital or lowercase
    if ord(letter) >= 65 and ord(letter) <= 90:
       return True
    elif ord(letter) >= 97 and ord(letter) <= 122:
       return True
    else:
       return False
