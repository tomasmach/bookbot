with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    


def give_unique_letters(data):
    alphabet_count = {}
    for i in data:
        if i.lower() in alphabet_count:
            alphabet_count[i.lower()] += 1
        else:
            alphabet_count[i.lower()] = 1
    
    return alphabet_count

def give_report(characters):
    for j in characters:
        print(f"The {j} character was found {characters[j]} times")

character_counter = give_unique_letters(file_contents)

print(character_counter)
give_report(character_counter)
