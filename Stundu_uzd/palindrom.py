words = ["level", "radar", "rotator", "deified", "Estere"]

for word in words:
    if word.lower() == word[::-1].lower():
        print(f'{word} is a palindrome')

    else:
        print(f'{word} is not a palindrome')