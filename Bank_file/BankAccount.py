
from typing import Tuple

from  PersonalInfo import *


class BankAccount(PersonalInfo):

    def __init__(self, Name: str, Id: str, Phone_number: str, Email_address: str, Balance: int = 0):
        """
        Constructor
        :param Name:
        :param Id:
        :param Phone_number:
        :param Email_address:
        :param Balance:
        """
        super().__init__(Name, Id, Phone_number, Email_address)
        self.Balance = Balance
        if not self.is_Valid_info():
            self.is_Valid_info()


    def Withdraw(self, Withdraw_Cash) -> int:
        """
        #Check for StudentBankAccount (cant be under 0)
        Withdraw money from self balance and commission
        :param num: amount of money
        :return: self deposit - amount of money - self commission
        """
        commission = 6
        #Check for StudentBankAccount (can't be under 0)
        if hasattr(self, 'college_name') or hasattr(self, 'company_Name'):
            if hasattr(self, 'college_name'):
                if self.Balance - (Withdraw_Cash + commission) < 0:
                    raise TypeError("Your Balance can't be negative number")
                else:
                    self.Balance -= Withdraw_Cash
                    self.Balance -= commission
                    return self.Balance
            elif hasattr(self, 'company_Name'):
                self.Balance -= Withdraw_Cash
                self.Balance -= commission * 1.5

        else:
            if Withdraw_Cash <= 0:
                raise TypeError("You can't withdraw 0 or negative number")
            else:
                self.Balance -= Withdraw_Cash
                return self.Balance

    def Deposit(self, Deposit_Cash) -> int:
        """
        Deposit money to self balance and withdraw commission
        :param num: amount of money
        :return: self balance + amount of money  - self commission
        """
        commission = 2
        #for BusinessBankAccount
        if hasattr(self, 'company_Name'):
            self.Balance += Deposit_Cash
            self.Balance -= commission * 1.5
        else:
            if Deposit_Cash == 0:
                raise TypeError("You can't Deposit 0 number")
            elif Deposit_Cash < 0:
                raise TypeError("You can't Deposit negative number")
            else:
                self.Balance += Deposit_Cash
                self.Balance -= commission
                return self.Balance

    def __str__(self):
        """
        to String
        :return:
        """
        return f"{super().__str__()}\nBalance : {self.Balance}"

    def is_Valid_info(self) -> Tuple[TypeError, bool]:
        """
        Function for validate client personal info and if exists error print typeError
        :return: True/False
        """

        if self.Name.index(' ', 1, len(self.Name)-2) != 0 and self.Name.replace(' ', '').isalpha() == True and\
                len(self.Name) < 0:

            raise TypeError("Invalid name")

        if not  '-' in self.Phone_number:
            raise TypeError("Invalid Phone number")

        if len(self.Phone_number) != 11:
            raise TypeError("Invalid Phone number")

        if not self.Email_address.index('@', 2, len(self.Email_address) - 6) != 0 and not\
                self.Email_address.index('.', self.Email_address('@', 2, len(self.Email_address) - 6) and not
                len(self.Email_address) - 2) != 0:

            raise TypeError("Invalid Email address")

        if len(self.Id) != 9:
            raise TypeError("Invalid id")
        else:
            for char in self.Id:
                if not char.isdigit():
                    raise TypeError("Invalid id")


        return True


def main():
    u1 = BankAccount("alex mircea", "123451788", "054-1232366", "ma242005@gmail.com", 1000)
    print(u1)
    print(u1)
    # u1.Withdraw(100)
    # u1.Deposit(10000)
    # print(u1)


if __name__ == '__main__':
    main()
