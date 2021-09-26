import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from MenuOfChoices import MenuOfChoices

MENU_OF_CHOICES = MenuOfChoices()

class FinancesUI():
    def __init__():
        pass
    def set_tax_to_emp(Finances):
        emp_id = int(input("Digite o ID do empregado: "))
        tax_value = float(input("Digite o valor da taxa: "))
        Finances.setTaxToEmployee(emp_id, tax_value)
        return Finances
    def set_sale_to_emp(Finances):
        emp_id = int(input("Digite o ID do empregado: "))
        date = MENU_OF_CHOICES.fill_in_date_format()
        value = float(input("Digite o valor da venda: "))
        comission = float(input("Digite o valor da comissão em %: "))
        comission = value*comission/100
        Finances.setSaleToEmployee(date, value, emp_id, comission)
        return Finances