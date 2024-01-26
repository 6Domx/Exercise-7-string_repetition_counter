# Pseudocode
# 1. Think of a string that we want to set as an example
# 2. Using the string example, identify how many times it will appear in an example sentence
# 3. Return the amount of times it was used

# Input for the sentence to be analyzed.
sentence_example = input("Please input something: ")
string_sample = input("What word would you like to look for? ")

# Command for the program to count how many "Miguel" was inputted by the user.
string_sample_count = sentence_example.count(string_sample)

# Printing of chosen word.
print("Your chosen word is: Miguel")

# Printing of how many times it appered.
print("It appered ", string_sample_count, " times.")
