class MenuOfChoices():
    def __init__(self):
        self.escolha = -1
    
    def main_menu(self):
        print("Escolha uma opção: \n0 - Opção de exibir detalhes do empregado\n1 - Opção para adicionar empregado\n2 - Opção de remover empregado\n3 - Opção de lançar um Cartão de Ponto\n4 - Opção para lançar um Resultado Venda\n5 - Opção para lançar uma taxa de serviço\n6 - Opção para alterar dados do empregado\n7 - Opção para rodar a folha de pagamento do dia\n8 - Opção da agenda de pagamento\n9 - Opção para criação de agenda de pagamento\n\n10 - Opção Sair\n\n")
       # print("0 - Opção de exibir detalhes do empregado\n1 - Opção para adicionar empregado\n2 - Opção de remover empregado\n3 - Opção de lançar um Cartão de Ponto\n4 - Opção para lançar um Resultado Venda\n5 - Opção para lançar uma taxa de serviço\n6 - Opção para alterar dados do empregado\n7 - Opção para rodar a folha de pagamento do dia\n8 - Opção da agenda de pagamento\n9 - Opção para criação de agenda de pagamento\n\n10 - Opção Sair\n\n")
        self.escolha = int(input("Digite a Opcao: "))
        return self.escolha
    def menu_employee_types(self):
        print("Tipo de empregado: \n1 - Comissionado\n2 - Horista\n3 - Salariado")
      #  print("1 - Comissionado\n2 - Horista\n3 - Salariado")
        self.escolha = int(input("Digite a opção: "))
        if self.escolha == 1: return "Comissioned"
        elif self.escolha == 2: return "Hourly"
        else: return "Salaried"
    def menu_payment_types(self):
        print("Metodos de pagamento: \n1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
       # print("1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
        self.escolha = int(input("Digite o metodo escolhido: "))
        if self.escolha == 1: return "AccountCredit"
        elif self.escolha == 2: return "CheckOnHands"
        else: return "DeliveryCheck"
    def menu_change_emp_details(self):
        print("Escolha o atributo que deseja alterar: \n1 - Tipo de empregado\n2 - Nome\n3 - RG\n4 - Endereço\n5 - Dados Bancários\n6 - Método de pagamento\n7 - Salário\n8 - Valor da hora de trabalho\n\n9 - Alterar\n10 - Sair sem alterar")
       # print("\n1 - Tipo de empregado\n2 - Nome\n3 - RG\n4 - Endereço\n5 - Dados Bancários\n6 - Método de pagamento\n7 - Salário\n8 - Valor da hora de trabalho\n\n9 - Alterar\n10 - Sair sem alterar")
        self.escolha = int(input("Digite a Escolha: "))
        return self.escolha
    def fill_in_bank_data(self):
        bankID = input("Digite o Banco: ")
        agency = input("Digite a Agencia: ")
        account = input("Digite a Conta: ")
        return bankID, agency, account
    def fill_in_date_format(self):
        print("Digite a Data: ")
        day = input("Digite o Dia: ")
        mounth = input("Digite o Mes: ")
        year = input("Digite o Ano: ")
        return year+"-"+mounth+"-"+day 