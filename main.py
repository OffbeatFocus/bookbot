def main():
    report("books/frankenstein.txt")

def count_words(text) -> int:
    return len(text.split())


def count_characters(text) -> dict:
    characters = {}
    for character in text.lower():
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters


def report(file):
    with open(file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        print(f"--- Begin report of {f.name} ---")
        print(f"{word_count} words found in the document\n")
        for character in dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True)):
            print(f"The '{character}' character was found {character_count[character]} times")
        print("--- End report ---")


main()
