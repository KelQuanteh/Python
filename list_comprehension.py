def convert_to_snake_case(pascal_or_camel_cased_string):
    # Use list comprehension to create a list of characters in snake_case
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the list of characters into a string and remove leading/trailing underscores
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Get input from the user
    camel_case = input('Enter CamelCase string: ')

    # Call the conversion function and print the result
    print(convert_to_snake_case(camel_case))

if __name__ == '__main__':
    # Execute the main function if the script is run directly
    main()
