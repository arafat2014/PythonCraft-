def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

user_input = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(user_input))
