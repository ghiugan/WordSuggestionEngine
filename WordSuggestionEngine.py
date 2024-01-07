"""
This program simulates an auto-fill search engine by providing user with a list of possible words based on user's typed input. 
The program stores words in a dictionary containing  two items: a list and a boolean. The list can contain another instance of dictionaries
and the boolean indicates if the end of a word is reached. If boolean is True, then the letters up to and including represents a word.

Refer to the Trie structure for a visual representation of the data structure used in this program.
"""

from typing import List

# Insert words into Trie structure
def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])    

"""
Returns the number of words encoded in data. 
"""
def count_words(data)->int:
    if not data:
        return 0

    count = 0
    for key in data.keys():
        if data[key][1]:  # Check if the current node marks the end of a word
            count += 1
        count += count_words(data[key][0])  # Recursively count words 

    return count
    

"""
Returns True if and only if s is encoded within data. 
"""
def contains(data, s: str)-> bool:
    if s == "":
        return True
    
    if len(s) == 1:
        if s in data:
            return data[s][1]
        else:
            return False

    if s[0] in data:
        return contains(data[s[0]][0], s[1:])
    else:
        return False

"""
Returns the length of longest word encoded in data.
"""
def height(data)->int:
    if not data:
        return 0
    
    max_height = 0
    for key, value in data.items():
        current_height = 1 + height(value[0]) 
        max_height = max(max_height, current_height)

    return max_height

"""
Returns the number of words in data which starts with the string
prefix, but is not equal to prefix.
""" 
def count_from_prefix(data, prefix: str)-> int:
    if prefix == "":
        return count_words(data)

    prefix_trie = contains_string(data, prefix)

    if prefix_trie == None:
        return 0
    
    return count_words(prefix_trie)

"""
Returns Trie, associated with the last letter from s, if and only if s is found within data, otherwise returns None.
"""
def contains_string(data, s: str)-> dict:
    if s == "":
        return None
    
    if len(s) == 1:
        if s in data:
            return data[s][0]
        else:
            return None

    if s[0] in data:
        return contains_string(data[s[0]][0], s[1:])
    else:
        return None

"""
Returns a list of words which are encoded in data, and starts with
prefix, but is not equal to prefix. You may assume data is a valid
trie.
"""
def get_suggestions(data, prefix:str)-> List[str]:
    words = []
    
    if prefix == "":
        return get_all_words([data, False], prefix, words)

    prefix_trie = contains_string(data, prefix)

    if prefix_trie == None:
        return []
    
    get_all_words([prefix_trie, False], prefix, words)
    
     
    return words
    
"""
Returns all the words as a list of strings.
"""
def get_all_words(value, current_word, words) -> List[str]:
    
    # Check if the current letter marks the end of a word
    if value[1]:  
        words.append(current_word)

    for char, subtree in value[0].items():
        get_all_words(subtree, current_word + char, words)

    return words   

def main():
    trie_data = {}

    print("Welcome to the Word Suggestion Program!")

    while True:
        user_input = input("1. Add a word\n2. Get suggestions\n3. Exit\nChoose an option (1/2/3): ").strip()

        if user_input == '1':
            word_to_add = input("Enter a word to add to the trie: ").strip().lower()
            insert(trie_data, word_to_add)
            print(f"'{word_to_add}' added to the trie!")

        elif user_input == '2':
            search_word = input("Enter a word to get suggestions: ").strip().lower()
            suggestions = get_suggestions(trie_data, search_word)
            
            if suggestions:
                print("Suggestions:", suggestions)
            else:
                print("No suggestions found.")

        elif user_input == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()