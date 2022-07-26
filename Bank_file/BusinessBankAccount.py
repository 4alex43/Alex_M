from business_info import *
from BankAccount import *


class BusinessBankAccount(BankAccount, Business_info):
    def __init__(self,name: str, id: str,phone_number: str, email: str ,company_Name: str, Tax_Number: str,
                 restriction: str, Violates_the_law: bool, Fee_debts: bool, address: str, Balance: int = 0):
        """
        Constructor
        :param name:
        :param id:
        :param phone_number:
        :param email:
        :param company_Name:
        :param Tax_Number:
        :param restriction:
        :param Violates_the_law:
        :param Fee_debts
        :param address
        :param Balance:
        """
        super().__init__(name,id,phone_number,email,Balance)
        Business_info.__init__(self,company_Name, Tax_Number, restriction, Violates_the_law, Fee_debts, address)


    def __str__(self):
        """
        To String
        :return:
        """
        return f"{super().__str__()},{Business_info.__str__(self)}"

def main():
    a1 = BusinessBankAccount("alex mircea", "123456780", "054-1232366", "ma242005@gmail.com", "CompayName","123456",
                             "no limit",False,False,"address")
    a1.Deposit(100)
    print(a1)

    # u1.Withdraw(100)
    # u1.Deposit(10000)
    # print(u1)


if __name__ == '__main__':
    main()















