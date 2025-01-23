import hashlib


def generate_hash():
    
    salt = "101224172"
    password = ""
    hashed_password = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    
    return hashed_password
    
    
if __name__ == "__main__":
    hashed_password = generate_hash()
    
    print(hashed_password)
    