import hashlib
import string
import itertools

student_number = "101224172"
last_two_digits = student_number[-2:]
target = f"c0ffee{last_two_digits}"

def password_generator():
    constraints = string.ascii_lowercase + string.digits
    length = 5
    
    while True:
        
        for password_tuple in itertools.product(constraints, repeat=length):
            password = ''.join(password_tuple)
            hashed_password = generate_hash(password=password)
            
            if str(hashed_password).startswith(target):
                return password, hashed_password
        
        
        length += 1
        
        if length > 16:
            print("Max length reached! ; resetting...")
            length = 5

def generate_hash(password):
    salt = student_number
    return hashlib.sha256((password + salt).encode()).hexdigest()

if __name__ == "__main__":
    password, hashed_password = password_generator()
    if password:
        print(f"Password found: {password}")
        print(f"Hashed Password : {hashed_password}")
    else:
        print("No password found within the constraints.")
