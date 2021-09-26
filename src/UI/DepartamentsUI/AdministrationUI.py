class AdministrationUI():
    def __init__(self):
        self.schedule = None
    def change_emp_paydate(Administration):
        emp_id = int(input("Digite o ID do empregado: "))
        i = 1
        prazo = Administration.get_paySchedules()
        for p in prazo:
            print(i, "- ", p, "\n")
            i += 1
        t = int(input("Opcao: "))
        Administration.setOnlyOneEmpPayDate(emp_id, prazo[t-1])
        return Administration    
    def fill_in_paydate_format():
        t = int(input("1 - semanal\n2 - quinzenal\n3 - mensal\n0 - Sair\n"))
        prazo = ["semanal", "quinzenal", "mensal"]
        print("Digite o dia\n")
        if t == 3:
            print("Caso seja o ultimo dia util do mes, digite '$'\n")
        day = input("Dia: ")
        return prazo[t-1]+"-"+day
    def create_new_schedule(Administration):
        new_schedule = []
        tam = int(input("Digite quantidade de datas que deseja criar? "))
        for i in range(tam):
            new_schedule.append(AdministrationUI.fill_in_paydate_format())
        Administration.set_paySchedules(new_schedule)
        return Administration
