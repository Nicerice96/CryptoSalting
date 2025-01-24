import hashlib
import string
from os import urandom
from base64 import b64encode

if __name__ == "__main__":
    len = 16
    salt_constraints = string.ascii_lowercase + string.digits
    
    