from BankAccount import *


class StudentBankAccount(BankAccount):
    def __init__(self, Name: str, Id: str, Phone_number: str, Email_address: str, college_name: str, Balance: int = 0):
        """
        Constructor,
        Data are checked immediately after initialization
        :param Name:
        :param Id:
        :param Phone_number:
        :param Email_address:
        :param college_name:
        :param Balance:
        """
        if Balance < 0:
            raise TypeError("Student can’t have negative Balance!!!")

        super().__init__(Name, Id, Phone_number, Email_address, Balance)
        self.college_name = college_name

    def __str__(self) -> str:
        return f"Name: {self.Name}\nId: {self.Id}\nPhone number: {self.Phone_number}" \
               f"\nEmail_address: {self.Email_address}\nBalance: {self.Balance}" \
               f"\ncollege name: {self.college_name}"

def main():
    u1 = StudentBankAccount("alex mircea", "123456789", "054-5362644", "ma242005@gmail.com", "ort", 106)
    u1.Deposit(100)
    print(u1)

if __name__ == '__main__':
    main()

