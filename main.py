import sys
import stats

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
    
def report():
    # getting the path from input
    
    book_path = sys.argv[1]
    
    #call functions
    
    num_words = stats.main(book_path)
    letter_dict = stats.character_counts(book_path)
    sorted_chars= stats.sort_chars(letter_dict)

    
    
    # printing the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    #the actual report
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")
    
report()