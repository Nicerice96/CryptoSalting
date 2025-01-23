import hashlib

student_number = "101224172"
last_two_digits = student_number[-2:]
target = f"c0ffee{last_two_digits}"
def open_file():
    file = open("10-million-password-list-top-1000000.txt", "r")
    
    return file.readlines()
    
    

def generate_hash(password_list):
    
    salt = "101224172"
    
    for password in password_list:
        password = password.strip()
        hashed_password = hashlib.sha256(password.encode() + salt.encode()).hexdigest
        
        if "target" in str(hashed_password):
            return True
        
    return False


    
    
    
if __name__ == "__main__":
    
    password_list = open_file()
    
    print(generate_hash(password_list=password_list))
    
    

    