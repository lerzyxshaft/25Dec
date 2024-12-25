import os
import random
import string

length = 13
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed(os.urandom(1024))

print(''.join(random.choice(chars) for _ in range(length)))
