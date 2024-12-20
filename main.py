with open("books/frankenstein.txt") as f:
    file_contents = f.read()



def give_unique_letters(data):
    alphabet_count = {}
    for i in data:
        if i.isalpha():
            if i.lower() in alphabet_count:
                alphabet_count[i.lower()] += 1
            else:
                alphabet_count[i.lower()] = 1

    return alphabet_count

def give_report(characters):
    for char, count in characters:
        print(f"The {char} character was found {count} times")

character_counter = give_unique_letters(file_contents)
sorted_characters = sorted(character_counter.items(), key=lambda x: x[1], reverse=True)

give_report(sorted_characters)
