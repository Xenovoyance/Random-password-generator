import string
import random
import subprocess 

## Creeate a string of upper- and lower-case letters, numbers and punctation marks. Out of this string, generate strings of default 25 char
def password_generator(size=25, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + "!?/!?/.,:"):
    return ''.join(random.choice(chars) for _ in range(size))

generated_password = password_generator()
print("INFO >> Password generated:", generated_password)

# Try to copy the generated password to clipboard (MacOS)
try:
    subprocess.run("pbcopy", universal_newlines=True, input=password_generator())
    print('INFO >> Password pasted to clipboard (MacOS)')
except FileNotFoundError:
    print('INFO >> Not running MacOS')

# Try to copy the generated password to clipboard (Windows)
try:
    subprocess.run("clip", universal_newlines=True, input=password_generator())
    print('INFO >> Password pasted to clipboard (Windows)')
except FileNotFoundError:
    print('INFO >> Not running Windows')

# Try to copy the generated password to clipboard (Linux)
#try:
#    subprocess.run("xclip", universal_newlines=True, input=password_generator())
#    print('INFO >> Password pasted to clipboard (Linux/xclip)')
#except FileNotFoundError:
#   print('INFO >> Not running Linux')