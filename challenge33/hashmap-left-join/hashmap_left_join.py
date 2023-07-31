
def left_join(synonyms_map, antonyms_map):
    joined_data = {}

    for word, synonym in synonyms_map.items():
        antonym = antonyms_map.get(word, None)
        joined_data[word] = (synonym, antonym)

    return joined_data

if __name__=="__main__":
    synonyms_map = {
        'happy': 'joyful',
        'sad': 'unhappy',
        'big': 'large',
        'small': 'tiny'
    }

    antonyms_map = {
        'happy': 'unhappy',
        'small': 'big',
        'big': 'small'
    }

    result = left_join(synonyms_map, antonyms_map)
    print(result)
