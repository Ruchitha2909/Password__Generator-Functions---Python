import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
    '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", ',', '.',
    '<', '>', '?', '/', '`', '~'
]

def get_user_choices():
    length = int(input("Enter password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, include_letters, include_numbers, include_symbols
  
def generate_password(length, include_letters, include_numbers, include_symbols):
    char_pool = []
    if include_letters:
        char_pool.extend(letters)
    if include_numbers:
        char_pool.extend(numbers)
    if include_symbols:
        char_pool.extend(symbols)

    if not char_pool:
        return "Error: No character types selected!"

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    length, include_letters, include_numbers, include_symbols = get_user_choices()
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print("\nGenerated Password:", password)

main()
