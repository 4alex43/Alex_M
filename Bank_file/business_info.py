class Business_info:
    def __init__(self, company_Name: str, Tax_Number: str, restriction: str, Violates_the_law: bool,
                 Fee_debts: bool, address: str):
        """
        Constructor
        :param company_Name:
        :param Tax_Number:
        :param restriction:
        :param Violates_the_law:
        :param Fee_debts:
        :param address:
        """
        self.company_Name = company_Name
        self.Tax_Number = Tax_Number
        self.restriction = restriction
        self.Violates_the_law = Violates_the_law
        self.Fee_debts = Fee_debts
        self.address = address

    def __str__(self):
        """
        to String
        :return:
        """
        return f"\ncompany name : {self.company_Name}\nTax number : {self.Tax_Number}\nrestriction: {self.restriction}" \
               f"\nViolates the law: {self.Violates_the_law}\nFee_debts: {self.Fee_debts}\nAddress: {self.address}"


def main():
    u1 = Business_info("CompayName","123456","no limit",False,False,"NewYORK")
    print(u1)
    # u1.Withdraw(100)
    # u1.Deposit(10000)
    # print(u1)


if __name__ == '__main__':
    main()


