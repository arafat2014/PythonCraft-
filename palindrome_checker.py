def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

user_input = input("Enter a word: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
