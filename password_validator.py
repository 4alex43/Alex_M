import sys, os
# Password validation in Python
# Function to validate the password
def password_check(passwd):
    """
        check if have:
        have equal or bigger digits than 10
        Last 1 upperCase
        Last 1 lowerCase
        Last 1 digit(number)
        in the password
        :param passwd: str
        :return: return 0(valid)(green)/1(invalid and error comments)(red)
    """
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
        
    return val


# Main method
def main():
    os.system("")
    res =""
    if sys.argv[1] == "-f":#If the option "-f" is added the password should be retrieved from a file
        if len(sys.argv) == 2:
            print("Error don't have a path")
        else:#read password from a file
            f = open(sys.argv[2], 'r')
            res = password_check(f.readline())
            f.close()
    else:
        res = password_check(sys.argv[1])

    if (res == 0):
        print('\033[0;32m' + str(res) + '\033[0m')#color green
    else:

        print('\033[91m' + str(res) + '\033[0m')#color red


main()
