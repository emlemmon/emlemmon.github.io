def prompt_filename():
    filename = input("Please enter a file: ")
    return filename

def main():
    name_of_file = prompt_filename()
    print("Opening file " + name_of_file)
    user_word = get_word()
    parse_file(name_of_file, user_word)
    print("The word pride occurs " + str(parse_file(name_of_file, user_word)) + " times in the file.")

def parse_file(name_of_file, word_to_match):
    opened_file = open(name_of_file, "r")
    count = 0
    for line in opened_file:
        words = line.split()
        words = [word.strip('.,!;()[]?') for word in words]
        for match in words:
            if word_to_match.lower() in match.lower():
                count += 1
    opened_file.close()
    return count

def get_word():
    return input("Enter a word to count: ")

if __name__ == "__main__":
    main()