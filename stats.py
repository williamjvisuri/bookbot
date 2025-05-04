
def sort_on(dict):
    return dict["num"]

def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    character_dict = {}
    text = text.lower()
    for character in text:
        if character not in character_dict:
            character_dict[character] = 0
        character_dict[character] += 1
    return character_dict

def sort_dict(dictionary):
    list_of_dicts = []
    for key, value in dictionary.items():
        list_of_dicts.append({"char": key, "num": value})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
