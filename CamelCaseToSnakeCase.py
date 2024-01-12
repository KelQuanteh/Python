def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []

    # Iterate through each character in the input string
    for char in pascal_or_camel_cased_string:
        # Check if the character is uppercase
        if char.isupper():
            # If uppercase, add an underscore before the lowercase version of the character
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            # If not uppercase, simply append the character to the list
            snake_cased_char_list.append(char)

    # Join the list of characters into a string
    snake_cased_string = ''.join(snake_cased_char_list)

    # Remove leading and trailing underscores (if any)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

def main():
    # Get input from the user
    camel_case = input('Enter CamelCase string: ')

    # Call the conversion function and print the result
    print(convert_to_snake_case(camel_case))

if __name__ == '__main__':
    # Execute the main function if the script is run directly
    main()
