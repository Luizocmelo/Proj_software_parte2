import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from RegisterTools.Sales import Sales
from RegisterTools.EmployeesPayCheck import EmployeesPayCheck
from RegisterTools.EmployeeBankData import EmployeeBankData

REGISTER = EmployeesPayCheck()

class Finances():
    def __init__(self):
        self.__sales = []
        self.__paymentRegister = []
    def get_sales(self): #Acessos
        return self.__sales
    def set_sales(self, new_list):
        self.__sales = new_list    
    def get_paymentRegister(self):
        return self.__paymentRegister
    def set_paymentRegister(self, new_payList):
        self.__paymentRegister = new_payList
      # Funções proprias   
    def add_employee_finances(self, emp_id, value_to_receive, bankID, agency, account, paymentMethod):
        e = EmployeeBankData(emp_id, value_to_receive, bankID, agency, account, paymentMethod)
        REGISTER.add_employee_payCheck(e)    
    def remove_employee_fin(self, emp_id):
        REGISTER.remove_emp(emp_id)
    
    def change_emp_fin_data(self, emp_id, bankID=None, agency=None, account=None, paymentMethod=None):
        REGISTER.change_emp_data(emp_id, bankID, agency, account, paymentMethod)
    
    def show_emp_details(self, emp_id):
        e = REGISTER.getOnlyEmpPayCheck(emp_id)
        if e: print(e)
        else: print("\n\nO empregado informado não foi encontrado ou nao existe!\n\n")    
    def setSaleToEmployee(self, date, value, emp_id, comission):
        if REGISTER.getOnlyEmpPayCheckIndex(emp_id):
            s = Sales(date, value, emp_id, comission)
            self.__sales.append(s)
            print(s)
        else: print("\n\nO empregado informado não foi encontrado ou nao existe!\n\n")
    def setTaxToEmployee(self, emp_id, tax_value):
        i = REGISTER.getOnlyEmpPayCheckIndex(emp_id)
        if i >= 0:
            REGISTER.employees_paycheck[i].add_tax_to_discount(tax_value)
            print(REGISTER.employees_paycheck[i])
    def payEmployees():
        pass
