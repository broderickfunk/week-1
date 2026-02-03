

# add code below ...
import string

# exercise 1
def palindrome(text):
    """Return True if `text` is a palindrome, ignoring case, spaces, and punctuation.

    A palindrome reads the same forwards and backwards after normalising.
    Examples: "racecar", "Nurses Run", "Sit on a potato pan, Otis."
    """
    cleaned = []

    for char in text.lower():
        if char.isalnum():
            cleaned.append(char)

    cleaned_text = "".join(cleaned)
    return cleaned_text == cleaned_text[::-1]

print(palindrome("combo"))

# exercise 2
def parentheses(sequence):
    """Return True if the parentheses in `sequence` are balanced.

    Parentheses are balanced if every opening '(' has a matching ')',
    parentheses are properly nested, and no closing parenthesis appears
    before its corresponding opening parenthesis.
    """
    count = 0

    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

            if count < 0:
                return False

    return count == 0

print(parentheses("(()hello((())()))"))