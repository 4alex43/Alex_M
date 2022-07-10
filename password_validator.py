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
    res =""
    if sys.argv[1] == "-f":
        if len(sys.argv) == 2:
            print("Error don't have a path")
        else:
            f = open(sys.argv[2], 'r')

            res = password_check(f.readline())
            f.close()
    else:
        res = password_check(sys.argv[1])

    if (res == 0):
#Dont need in the h.w        #print(f"{str(sys.argv[1])}\n",file=open('password.txt', 'a+'))#add string to file in new line everyTime
        print('\033[0;32m' + str(res) + '\033[0m')
    else:

        print('\033[91m' + str(res) + '\033[0m')


main()
