file_name = input("Enter file: ")
a_file = open(file_name, "r")

word_count = 0
line_count = 0
for line in a_file:
    line_count += 1
    word_count += len(line.split())

print("The file contains " + str(line_count) + " lines and " + str(word_count) + " words." )

a_file.close()