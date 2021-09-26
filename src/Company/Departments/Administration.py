class Administration():
    def __init__(self):
        self.__paySchedules = ["semanal-sexta", "quinzenal-sexta", "mensal-$"]
        self.__employeesPayDate = []
    def get_paySchedules(self): #Acessos
        return self.__paySchedules
    def set_paySchedules(self, new_paySchedules):
        self.__paySchedules = new_paySchedules
        print(new_paySchedules)
    def get_employeesPayDate(self):
        return self.__employeesPayDate
    def add_employeePayDate(self, emp_id, emp_type): #Funçoes proprias
        if emp_type == "Hourly":
            self.__employeesPayDate.append({'id':emp_id, 'date':'semanal-sexta'})
        elif emp_type == "Comissioned":
            self.__employeesPayDate.append({'id':emp_id, 'date':'quinzenal-sexta'})
        else: self.__employeesPayDate.append({'id':emp_id, 'date':'mensal-$'})
    def getOnlyOneEmpPayDate(self, emp_id):
        for employee in self.__employeesPayDate:
            if employee['id'] == emp_id:
                return employee['date']
    def setOnlyOneEmpPayDate(self, emp_id, new_payDate):
        for employee in self.__employeesPayDate:
            if employee['id'] == emp_id:
                employee['date'] = new_payDate
                print(employee)
    def remove_employee_adm(self, emp_id):
        for e in self.__employeesPayDate:
            if e['id'] == emp_id:
                self.__employeesPayDate.remove(e)