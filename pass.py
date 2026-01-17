import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 for security!")
        return ""
    
    # All possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def check_strength(password):
    length = len(password)
    if length < 6:
        return "Weak"
    elif length < 10:
        return "Medium"
    else:
        return "Strong"

def main():
    print("🔐 Password Generator & Strength Checker")
    
    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            length = int(input("Enter password length: "))
            pwd = generate_password(length)
            if pwd:
                print(f"Generated Password: {pwd}")
                print(f"Strength: {check_strength(pwd)}")
        elif choice == "2":
            pwd = input("Enter password to check: ")
            print(f"Password Strength: {check_strength(pwd)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
