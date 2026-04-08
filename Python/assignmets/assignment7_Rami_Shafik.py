#Rami Shafik 100971729

######################################## set.py #########################################

sentence = input("Enter a sentence with special characters (e.g., ? or -): ")
sentence_list = list(sentence)

vowels_set = set ("aeiouAEIOU")
alphabet_set = set ("qwertyuiopasdfghjklkzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

def checkvowelsConsonants(sentence):
    vowels = 0
    consonants = 0
    
    for i in sentence: 
        if i in alphabet_set:
            if i in vowels_set:
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    return vowels, consonants

vowels, consonants = checkvowelsConsonants(sentence)

while True:
    print("Options:")
    print("[1] Print the number of vowels and consonants")
    print("[2] Exit the program")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print(f"The number of vowels is {vowels} and consonants is {consonants}")
    elif choice == "2":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

######################################## set.py #########################################

def main():

    keywordsList = [
        "and", "del", "global", "while", "for", "in", "else", "print","return", "import", 
        "if", "elif", "break", "continue", "while","for", "return", "if", "print", "else"
    ]
    
    dictionary = {}

    for i in keywordsList:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    
    print("Keyword_name".ljust(20) + "Count")
    print("-" * 25)
    for keyword, count in sorted_dictionary.items():
        print(keyword.ljust(20), count)

main()