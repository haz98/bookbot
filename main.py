def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    list = report(get_each_char(text))



def sort_on(dict):
    return dict["num"]    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_each_char(text):
    diction = {}
    lower_text = text.lower()
    for p in lower_text:
        if(p in diction):
            diction[p] += 1
        else: diction[p] = 1
    return diction

def report(dict):
    list = []
    for p in dict:
        list.append({'char':p, 'num':dict[p]})

    list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    for dic in list:
        if dic["char"].isalpha():
            print(f"the '{dic["char"]}' character was found {dic["num"]} times")
    print("--- End report ---")
    return list



main()