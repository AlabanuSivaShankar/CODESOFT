import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 to include a mix of characters."

   
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars),
    ]

    
    all_chars = lower_case + upper_case + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("\nEnter the desired password length (minimum 4): "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
        choice = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
