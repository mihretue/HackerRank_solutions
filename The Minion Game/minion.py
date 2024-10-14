# Input word
word = "BANANA"

# Define vowels
vowels = "AEIOU"
vowel_list = []
consonants = []
# Iterate through each character in the word
for char in word:
    # Check if the character is a vowel
    if char in vowels:
        vowel_list.append(char)
    # Check if the character is a consonant (and is a letter)
    elif char.isalpha():
        consonants.append(char)
# print(vowel_list)

# List to hold sentences or substrings 
starting_with_vowels = []
starting_with_consonants = []


# Loop over the word to find all substrings starting with 'vowel or consonant'
for i in range(len(word)):
    if word[i] in vowel_list:
        # Add substrings starting to the list
        for j in range(i + 1, len(word) + 1):
            starting_with_vowels.append(word[i:j])
    else:
        for j in range(i+1, len(word) +1):
            starting_with_consonants.append(word[i:j])

# Display the results
print("Substrings starting with 'vowels':", starting_with_vowels)
print("Kevin", len(starting_with_vowels))
print("Substrings starting with 'consonants':", starting_with_consonants)
print("Stuart", len(starting_with_consonants))
