
def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        words_length = count_words(content)
        letters = count_letters(content)
        print(f"number of words is {words_length}")
        print_report(letters)

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    count = {}
    lower_text = text.lower()
    for letter in lower_text:
        current_count = count.get(letter, 0) 
        count[letter] = current_count + 1
    
    return count
    

def print_report(letters):
    sorted_dict = dict(sorted(letters.items(), key=lambda x:x[1], reverse=True))
    for key in sorted_dict:
        print(f"The '{key}' character was found {sorted_dict[key]} times")


main()