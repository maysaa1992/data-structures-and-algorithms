def repeated_word(string):
    string = string.lower()
    words = string.split()
    word_split = []

    for word in words:
        if word in word_split:
            return word
        else:
            word_split.append(word)

    return None

if __name__=="__main__":
    input_string = "This is a sample string with repeated words like is and a and sample."
    result = repeated_word(input_string)
    print(result)  # Output: "is"