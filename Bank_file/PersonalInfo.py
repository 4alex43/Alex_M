

class PersonalInfo:
    def __init__(self, Name: str, Id: str, Phone_number: str, Email_address: str):
        """
        Constructor
        :param name:
        :param id:
        :param phone_number:
        :param email_address:
        """
        self.Name = Name
        self.Id = Id
        self.Phone_number = Phone_number
        self.Email_address = Email_address

    def __str__(self) -> str:
        """
        to String
        :return: str of object
        """
        return f"Name: {self.Name}\nId: {self.Id}\nPhone number: {self.Phone_number}\nEmail_address: {self.Email_address}"
