'''
    script: CIS129_JohnVarela_ExtraCredit.py
    action: a. gets english phrase from user
            b. translates english phrase to pig latin
            c. prints translated phrase
    author: John Alex Varela
    date:   12/09/2024
'''

def main():
    '''
    main method to get input from the user and then loop them if their input is
    incorrect and prints a translated phrase.

    action: gets input from user
            prints user input translated to Pig Latin
            asks user for new input if user input was invalid
    input: english phrase from user
    output: user's input translated to pig latin
    return: none
    '''
    # conditional for while loop
    i = True

    # while loop to ask for new user input if user input is invalid
    while i:
        english_phrase = input("Please enter a phrase in english: ")

        # try clause to check if user input is valid
        try:
            translation = translate(english_phrase)
            print(f'Pig Latin Translation: {translation}')
            i = False
        except IndexError:
            print("Index Error Please Try again")
            

    

def translate(phrase):
    '''
    function to translate english phrase to pig latin

    action: splits user input into a list for each word in the phrase
            checks if a word starts with a vowel
            translates based on if word starts with a vowel
    input: none
    output: translated phrase
    return: translated phrase
    '''

    # variable for naming vowels
    vowels = "aeioAEIOU"

    # variable to split my phrase into lists
    english_words = phrase.split()

    # list to hold my translated phrase
    latin_words = []
    
    # for loop to translate each word in user's phrase and append each word
    # to the latin_words list then joins them into one string to send to main
    for word in english_words:
        if word[0] in vowels:
            # in: after
            # out: afteray
            latin = word + "ay"
        else:
            # in: hello
            # out: ellohay
            latin = word[1:] + word[:1] + 'ay'
        latin_words.append(latin)
    return " ".join(latin_words)

main()