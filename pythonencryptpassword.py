import bcrypt

def hash_password(password):
    """
    Hashes a password securely using bcrypt.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The hashed password.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

if __name__ == "__main__":
    plaintext_password = "mySecureP@ssword123"
    hashed_password = hash_password(plaintext_password)
    print("Hashed Password:", hashed_password)
