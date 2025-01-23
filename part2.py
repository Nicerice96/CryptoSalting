import hashlib
import itertools
import string


def find_salt(password, hashed_password):
    
    salt_constraints = string.ascii_lowercase
    salt_len = 8
    
    for salt_tuple in itertools.product(salt_constraints, repeat=salt_len):
        salt = ''.join(salt_tuple)
        
        generated_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        
        if (hashed_password == generated_hash):
            return salt
        
    return None

if __name__ == "__main__":
    
    password = "comp2108"
    hashed_password = "9f02b0fd48e9211a5a33ae3321b942896e4ebb0cb267fdfff53fa58cf8c56f24"
    
    salt = find_salt(password=password, hashed_password=hashed_password)
    
    print("Salt found: " + str(salt))