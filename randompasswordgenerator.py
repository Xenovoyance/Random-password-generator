import string
import random

## Creeate a string of upper- and lower-case letters, numbers and punctation marks. Out of this string, generate strings of default 25 char
def password_generator(size=25, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

print(password_generator())
