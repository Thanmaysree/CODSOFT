import random
import string

def calculate_strength(password):
    score = 0
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        score += 10

    if any(c.islower() for c in password):
        score += 15
    if any(c.isupper() for c in password):
        score += 15
    if any(c.isdigit() for c in password):
        score += 20
    if any(c in string.punctuation for c in password):
        score += 20

    return min(score, 100)

def generate_password(length, strength, memorable, keyword):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if strength == 1:
        chars = lower + upper
    elif strength == 2:
        chars = lower + upper + digits
    else:
        chars = lower + upper + digits + symbols

    password = ""

    if memorable == 'y':
        words = ["Sun", "Moon", "Star", "Sky", "Fire", "Tree"]
        password = random.choice(words)
        if keyword:
            password += keyword
        password += str(random.randint(10, 99))
        password += random.choice(symbols)
    else:
        for _ in range(length):
            password += random.choice(chars)

        if keyword:
            pos = random.randint(0, len(password))
            password = password[:pos] + keyword + password[pos:]

    return password[:length]

# ~MAIN PROGRAM 

print("\n🔐 PASSWORD GENERATOR 🔐")

print("\nPurpose of password:")
print("1. Social Media")
print("2. Banking")
print("3. College Portal")
print("4. WiFi")

purpose = int(input("Enter choice: "))

if purpose == 2:
    length = 14
elif purpose == 4:
    length = 10
else:
    length = int(input("Enter password length: "))

print("\nStrength Mode:")
print("1. Easy")
print("2. Medium")
print("3. Strong")
strength = int(input("Choose strength: "))

memorable = input("Memorable password? (y/n): ").lower()
keyword = input("Enter keyword (optional, press Enter to skip): ")

password = generate_password(length, strength, memorable, keyword)
score = calculate_strength(password)

print("\n🔑 Generated Password:", password)
print("📊 Strength Score:", score, "%")

if score >= 80:
    print("Rating: VERY STRONG 🔐")
elif score >= 60:
    print("Rating: STRONG ✅")
else:
    print("Rating: WEAK ⚠ Improve length or symbols")

