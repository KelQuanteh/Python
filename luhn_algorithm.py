def verify_card_number(card_number):
    # Initialize the sum of odd digits
    sum_of_odd_digits = 0
    
    # Reverse the card number for easier iteration
    card_number_reversed = card_number[::-1]
    
    # Extract odd digits from the reversed card number
    odd_digits = card_number_reversed[::2]

    # Calculate the sum of odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize the sum of even digits
    sum_of_even_digits = 0
    
    # Extract even digits from the reversed card number
    even_digits = card_number_reversed[1::2]
    
    # Calculate the sum of even digits after doubling each digit
    for digit in even_digits:
        number = int(digit) * 2
        
        # If the doubled number is greater than or equal to 10, split and add the digits
        if number >= 10:
            number = (number // 10) + (number % 10)
        
        sum_of_even_digits += number

    # Calculate the total sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    
    # Check if the total sum is divisible by 10 (valid card number)
    return total % 10 == 0

def main():
    # Example card number with spaces and hyphens
    card_number = '4111-1112-4555-1141'
    
    # Remove spaces and hyphens from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Verify the validity of the card number and print the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Run the main function
main()
