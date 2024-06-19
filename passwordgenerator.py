import random
import string

class PasswordGenerator:
    def __init__(self, length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_special = use_special
        self.characters = self._initialize_characters()

    def _initialize_characters(self):
        characters = ''
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_special:
            characters += string.punctuation
        if not characters:
            raise ValueError("At least one character set must be enabled")
        return characters

    def generate(self):
        if self.length < 1:
            raise ValueError("Password length must be at least 1")
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password

def validate_input(prompt, valid_responses):
    while True:
        response = input(prompt).strip().lower()
        if response in valid_responses:
            return response
        print(f"Invalid response. Please enter one of {valid_responses}.")

def evaluate_strength(password):
    length_score = min(len(password) / 4, 1) * 25
    variety_score = (len(set(password) & set(string.ascii_uppercase)) > 0) * 25
    variety_score += (len(set(password) & set(string.ascii_lowercase)) > 0) * 25
    variety_score += (len(set(password) & set(string.digits)) > 0) * 25
    variety_score += (len(set(password) & set(string.punctuation)) > 0) * 25
    total_score = length_score + variety_score
    if total_score >= 80:
        return "Strong"
    elif total_score >= 50:
        return "Medium"
    else:
        return "Weak"

def main():
    print("Welcome to the Enhanced Random Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length (minimum 1): "))
            if length < 1:
                print("Length must be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    use_uppercase = validate_input("Include uppercase letters? (y/n): ", ['y', 'n']) == 'y'
    use_lowercase = validate_input("Include lowercase letters? (y/n): ", ['y', 'n']) == 'y'
    use_digits = validate_input("Include digits? (y/n): ", ['y', 'n']) == 'y'
    use_special = validate_input("Include special characters? (y/n): ", ['y', 'n']) == 'y'

    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords < 1:
                print("Number of passwords must be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    generator = PasswordGenerator(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_digits=use_digits,
        use_special=use_special
    )

    passwords = []
    for _ in range(num_passwords):
        password = generator.generate()
        strength = evaluate_strength(password)
        passwords.append((password, strength))
        print(f"Generated password: {password} (Strength: {strength})")

if __name__ == "__main__":
    main()
