import random
import string

def generate_random_text(length=6):
    characters = string.ascii_letters + string.digits  # Includes uppercase, lowercase, and digits
    return ''.join(random.choices(characters, k=length))

# Example usage
print(generate_random_text())
