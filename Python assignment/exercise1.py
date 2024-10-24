def camel_to_snake(camel_str):
    snake_str = ''
    for char in camel_str:
        if char.isupper():
            snake_str += '_' + char.lower()
        else:
            snake_str += char
    return snake_str
camel_case = input("Enter a camel case variable name: ")
print("Snake case:", camel_to_snake(camel_case))
