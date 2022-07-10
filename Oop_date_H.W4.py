import datetime
from datetime import date, timedelta

class Date:

    def __init__(self, d: int, m: int, y: int):
        self.day = d
        self.month = m
        self.year = y

    def __str__(self):
        """
        This Date to str
        :return: str date
        """
        res = f"Date: {self.day}/{self.month}/{self.year}"
        return res

    def is_valid(self):
        """
        Check if input is valid
        :return: True or False
        """
        d = str(self.day)+"/"+str(self.month)+"/"+str(self.year)
        try:
            datetime.date(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def __eq__(self, other):
        """
        Check if this date equal to input date
        :param other:
        :return: True or False
        """
        day1 = date(self.year, self.month, self.day)
        day2 = date(other.year, other.month, other.day)
        return day1 == day2

    def __gt__(self, other):
        """
        Check if this date after input date
        :param other: input date
        :return: True or False
        """
        day1 = date(self.year, self.month, self.day)
        day2 = date(other.year, other.month, other.day)
        return day1 > day2

    def __lt__(self, other):
        """
        Check if this date before input date
        :param other: input date
        :return: True or False
        """
        day1 = date(self.year,self.month,self.day)
        day2 = date(other.year,other.month,other.day)
        return day1 < day2

    def __sub__(self, other):
        """
        Return date difference between to dates
        if this date before return a negative number
        :param other:input date
        :return: difference
        """
        day1 = date(self.year,self.month,self.day)
        day2 = date(other.year, other.month, other.day)
        res = day1 - day2
        return res.days


    def get_next_days(self, days_to_add= 1):
        """
        if do not input num up day 1
        Add input days to this date
        :param daysToAdd: int
        :return: Date,this date + daysToAdd
        """
        d1 = date(self.year, self.month, self.day)
        add_days = d1 + timedelta(days_to_add)
        res = Date(add_days.day, add_days.month, add_days.year)
        return res










