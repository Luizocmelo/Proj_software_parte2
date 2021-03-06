import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from BankData import BankData

class Company(BankData):
    def __init__(self, bankID, agency, account, name):
        super().__init__(bankID, agency, account)
        self.__name = name
    def set_name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name