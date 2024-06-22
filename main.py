def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_words(text)
    chars_dict = count_characters(text)
    chars_sorted_list = convert_to_sorted_list(chars_dict)

    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for dic in chars_sorted_list:
        if dic['char'].isalpha():
            print(f"The {dic['char']} character was found {dic['num']} times")
    print("--- End report ---")

def get_book_text(text_path):
    with open(text_path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def convert_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    
main()
