import hashlib
import string
import os
from os import urandom
import base64
from base64 import b64encode
import random


def generate_salts():
    """By using the operating system's random number generator (which is a CPRNG) as the "seed" for the random library, 
    we can turn the random library from a "PRNG" into a "CPRNG", as now the "source" of the number generator is TRULY random

    Returns:
        _type_: _description_
    """
    salt_constraints = string.ascii_lowercase + string.digits
    count = 0
    generated_salts = []
    while (count < 16):
            randombytes = os.urandom(16)
            random.seed(randombytes) #using the random bytes generated from urandom as the "source" of the randomness
            
            
            salt = ''.join(random.choices(salt_constraints, k=16))
            
            generated_salts.append(salt)
            count+=1
                
    return generated_salts
        
        


if __name__ == "__main__":
    
    generated_salts = generate_salts()
    
    for salt in generated_salts:
        print(salt)
   
    
    
    
    