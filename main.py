from stats import get_number_of_words,get_number_of_characters,get_dictionary,sort_dic
import sys

def get_book_text(book):
    with open(book) as b:
        file_contents = b.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_into_string = get_book_text(sys.argv[1])
    num_words = get_number_of_words(text_into_string)
    new_dic = get_number_of_characters(text_into_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_dics = get_dictionary(new_dic)
    list_of_dics.sort(reverse=True,key=sort_dic)
    for i in list_of_dics:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
        else:
            continue

main()