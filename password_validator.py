from string import ascii_letters, digits
import sys, os


# Password validation in Python
# using naive method

# Function to validate the password
def password_check(passwd):
    val = 0
    if len(passwd) < 10:
        print("length should be bigger then 10 digits")
        val = 1

    if not any(char.isdigit() for char in passwd):
        print("Password should have at least one numeral")
        val = 1

    if not any(char.isupper() for char in passwd):
        print("Password should have at least one uppercase letter")
        val = 1

    if not any(char.islower() for char in passwd):
        print("Password should have at least one lowercase letter")
        val = 1
#remove dont ask for it
    if set(passwd).difference(ascii_letters + digits):
        print("Password has special characters.")
        val = 1
    return val


# Main method
def main():
    os.system("")

    res = password_check(sys.argv[1])

    if (res == 0):
        print('\033[0;32m' + "Valid password" + '\033[0m')
    else:
        print('\033[91m' + "Invalid password" + '\033[0m')


main()
