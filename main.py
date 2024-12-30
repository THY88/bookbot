def main():
    filepath = "books/frankenstein.txt"
    doc = read_file(filepath)
    print_report(doc)

    
def count_word(doc):
    wordcount = len(doc.split())
    return wordcount

def char_count(doc):
    char_dict = {}
    for char in doc:
        if char.lower().isalpha():
            if char.lower() not in char_dict:
                char_dict[char.lower()] = 1
            else:
                char_dict[char.lower()] += 1
    return char_dict

def print_report(doc):
    print(f"{count_word(doc)} words found in the document")
    for k ,v in sorted(char_count(doc).items(), key=lambda x: x[1], reverse=True):
        print(f"The {k} character was found {v} times")
    print("--- End report ---")

def read_file(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

        
if __name__ == "__main__":
    main()