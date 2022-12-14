input_string = input("Enter text: ")
words = input_string.split(" ")
words = sorted(words, key = len, reverse = True)
for i in range(3):
    print (words[i])


