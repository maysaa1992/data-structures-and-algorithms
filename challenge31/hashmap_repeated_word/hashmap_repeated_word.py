def repeated_word(string):
        '''
        Find the first repeated word in a given string.

        This function takes a string as input and returns the first word that appears more than once
        (case-insensitive) in the string. If no repeated word is found, it returns None.
        
        '''        
        string = string.lower()
        words = string.split()
        word_set = set()  # Using a set as the hashtable for faster lookup

        for word in words:
            if word in word_set:
                return word
            else:
                word_set.add(word)

        return None

if __name__ == "__main__":
    input_string = "This is a sample string with repeated words like is and a and sample."
    result = repeated_word(input_string)
    print(result)  
