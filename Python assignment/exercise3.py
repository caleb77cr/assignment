def omit_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    return result

text = input("Enter a string of text: ")
print("Text without vowels:", omit_vowels(text))
