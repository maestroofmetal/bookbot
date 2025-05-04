
# getting text from file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


# counts the words in the specified file
def main(book_path):
    file_contents = get_book_text(book_path)
    num_words = len(file_contents.split())
    return book_path, num_words


# counts the unique characters in the source file
def character_counts(book_path):
    file_contents = get_book_text(book_path)
    letter_dict={}
    for letter in file_contents:
        if letter.lower() not in letter_dict:
            letter_dict[letter.lower()] = 1
        else:
            letter_dict[letter.lower()] += 1
    
    return letter_dict    

def sort_by_num(letter_dict):
    return letter_dict["num"]

def sort_chars(letter_dict):
    char_list = []
    for char, count in letter_dict.items():
        # unpacks the dictionary into tuples of key-value pairs
        # this way you can call on them.
        char_list.append({"char": char,"num": count})
        
    char_list.sort(reverse=True, key=sort_by_num)
    return char_list
