from BusinessBankAccount import *
from StudentBankAccount import *
from BankAccount import *
import statistics
import sys
import xml.etree.ElementTree as ET


class Bank(BankAccount):

    def __init__(self):
        """
        Main Bank Constructor
        """
        self.bank = {'StudentBankAccount': [], 'BankAccount': [], 'BusinessBankAccount': []}

    def __str__(self):
        """
        to String a = Student bank Accounts b = Bank accounts   c= 'BusinessBankAccounts
        :return:
        """
        student = 'Student bank Accounts : \n'
        bank = 'Bank accounts : \n'
        business = 'BusinessBankAccount \n'

        for i in range(len(self.bank['StudentBankAccount'])):
            student += f"{str(self.bank['StudentBankAccount'][i])}\n"

        for i in range(len(self.bank['BankAccount'])):
            bank += f"{str(self.bank['BankAccount'][i])}\n"

        for i in range(len(self.bank['BusinessBankAccount'])):
            business += f"{str(self.bank['BusinessBankAccount'][i])}\n"

        return f"{student} {bank} {business}"

    def load_and_parse_init_data(self, file):

        """
        Function for load and parse data from XML file to dictionary
        :return: dict with all data from XML
        """

        tree = ET.parse(sys.argv[1])
        root = tree.getroot()
        dict_ = {}

        for tag in root.findall('.account'):
            if tag.attrib['type'] == 'BankAccount':
                for el in tag.findall('.//'):
                    dict_[el.tag] = el.text

            if tag.attrib['type'] == 'BusinessBankAccount':
                for el in tag.findall('.//'):
                    dict_[el.tag] = el.text

            if tag.attrib['type'] == 'StudentBankAccount':
                for el in tag.findall('.//'):
                    dict_[el.tag] = el.text

        return root

    def add_new_account(self):
        """
        Function for add all accounts from XML file to Bank
        :return: new bank after add from xml
        """
        # Create variable with parse and load function
        accounts_for_adding = self.load_and_parse_init_data()

        for tag in accounts_for_adding.findall('.account'):

            if tag.attrib['type'] == 'BankAccount':
                bank_Account = BankAccount('None Name', '123456789', '054-0000000', 'test123@sela.co.il')

                for el in tag.findall('.//'):
                    if el.tag == 'name':
                        bank_Account.Name = el.text
                    if el.tag == 'id':
                        bank_Account.Id = el.text
                    if el.tag == 'phone':
                        bank_Account.Phone_number = el.text
                    if el.tag == 'email':
                        bank_Account.Email_address = el.text
                    if el.tag == 'balance':
                        bank_Account.Balance = el.text

                if not bank_Account.is_Valid_info():
                    raise bank_Account.is_Valid_info()
                self.bank['BankAccount'].append(bank_Account)

            if tag.attrib['type'] == 'StudentBankAccount':
                student_Account = StudentBankAccount('None Name', '123456789', '054-0000000', 'test123@sela.co.il',
                                                     'college')

                for el in tag.findall('.//'):
                    if el.tag == 'name':
                        student_Account.Name = el.text
                    if el.tag == 'id':
                        student_Account.Id = el.text
                    if el.tag == 'phone':
                        student_Account.Phone_number = el.text
                    if el.tag == 'email':
                        student_Account.Email_address = el.text
                    if el.tag == 'college':
                        student_Account.college_name = el.text
                    if el.tag == 'balance':
                        student_Account.Balance = el.text
                if not student_Account.is_Valid_info():
                    print(student_Account.Id)
                    raise student_Account.is_Valid_info()
                self.bank['StudentBankAccount'].append(student_Account)

            if tag.attrib['type'] == 'BusinessBankAccount':
                business_account = BusinessBankAccount("alex mircea", "123456780", "054-1232366", "tryMe123@gmail.com",
                                                       "CompayName","123456", "no limit", False, False, "address")

                for el in tag.findall('.//'):

                    if el.tag == 'name':
                        business_account.name = el.text
                    if el.tag == 'id':
                        business_account.id = el.text
                    if el.tag == 'phone':
                        business_account.phone = el.text
                    if el.tag == 'email':
                        business_account.email = el.text
                    if el.tag == 'company_Name':
                        business_account.company_Name = el.text
                    if el.tag == 'Tax_Number':
                        business_account.Tax_Number = el.text
                    if el.tag == 'restriction':
                        business_account.restriction = el.text
                    if el.tag == 'Violates_the_law':
                        business_account.Violates_the_law = el.text
                    if el.tag == 'Fee_debts':
                        business_account.Fee_debts = el.text
                    if el.tag == 'address':
                        business_account.address = el.text
                    if el.tag == 'Balance':
                        business_account.Balance = el.text
                if not business_account.is_Valid_info():
                    raise business_account.is_Valid_info()

                self.bank['BusinessBankAccount'].append(business_account)

    def withdraw_by_user_id(self, id: str, withdraw: int):
        """
        Function for withdraw money by id
        :param id: client id
        :param withdraw: amount of money
        :return: self deposit - amount of money - self commission
        """
        for k, v in self.bank.items():
            for objc in v:
                if id == objc.Id:
                    objc.Withdraw(withdraw)

    def deposit_by_user_id(self, id: str, deposit: int):
        """
        Deposit money to self balance by id
        :param id:
        :param Id: client id
        :param deposit: amount of money
        :return:
        """
        for k, v in self.bank.items():
            for objc in v:
                if id == objc.Id:
                    objc.Deposit(deposit)

    def calc_balance_statistics(self):
        """
        Function for calculate avg / median / 90th percentile and 10th
        percentile of balances of all already added clients of the bank
        :return: string with all data avg,median,90th,10th
        """
        avg = 0
        balances = []
        for k, v in self.bank.items():
            for objc in v:
                balances.append(objc.Balance)
                avg += objc.Balance

        prcntl_90 = avg * 0.9
        prcntl_10 = avg * 0.1
        avg /= len(balances)
        median = statistics.median(balances)
        result = f'Avg is          : {avg}\n' \
                 f'Median is       : {median}\n' \
                 f'90th percentile : {prcntl_90}\n' \
                 f'10th percentile : {prcntl_10}'
        return result

    def delete_by_user_id(self,id: str):
        d = []
        id = str(id)
        for k,v in self.bank.items():
            for account in range(len(v)):
                if v[account].Id != id:
                    d.append(v[account])

            self.bank[k] = d
            d = []


def main():
    b = Bank()

    if sys.argv[1] == "init.xml":
        ET.parse(sys.argv[1])
        b.load_and_parse_init_data()
        b.add_new_account()
        print(b)
        b.deposit_by_user_id("012345678", 1000)
        b.deposit_by_user_id("223344551", 100)
        b.deposit_by_user_id("888888881", 100000)
        res = b.calc_balance_statistics()
        print(res)
    else:
        raise TypeError("Something wrong, please check the file or path")


if __name__ == '_main_':
    main()

main()
